let table = '';
let enviar = document.querySelector('.iglesia-enviar');

enviar.addEventListener('click', (e) => {
    e.preventDefault();
    const form = document.querySelector('form');
    $.ajax({
        method: form.method,
        url: form.action,
        data: $('form').serialize(),
        success: (resp) => {
            if (resp.existe) {

                Toast.fire({
                    icon: 'success',
                    title: resp.message
                });
                if (resp.estado === 'Crear') {
                  
                }
                table.ajax.reload();
            }
            else{
                Toast.fire({
                    icon: resp.estado,
                    title: resp.message
                });
            }
        }
    });
});

const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    onOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
})

const getIglesia = () => {

    table = $('#listaTable').DataTable({
        "processing": true,
        "ajax": 'http://127.0.0.1:8000/iglesia/lista-iglesia',

        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
        },
        "columns": [

            { "title": "Nombre", "data": "nombre" },
            { "title": "Email", "data": "correo" },
            { "title": "Dirección", "data": "direccion" },
            { "title": "Teléfono", "data": "telefono" },
            { "title": "Estado", "data": "estado" },

            {
                title: "Acción",
                width: "22%",
                data: null,
                render: function(data, type, row, meta) {
                    return "<a href='/iglesia/editar/" + row.iglesia_id + "' class='btn btn-warning btn-sm'><i class='fa fa-edit'></i> Editar</a>   <a href='#' class='btn btn-danger btn-sm eliminar' onclick=getEliminar(" + row.iglesia_id + ") ><i class='fa fa-trash'></i> Eliminar</a>";
                }
            }
        ],
    });
};
getIglesia();

getEliminar = (id) => {

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Estas seguro(a)?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Si, Eliminiar!',
        cancelButtonText: 'No, cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            let timerInterval
            Swal.fire({
                title: 'Alerta de cierre automático!',
                html: 'Voy a cerrar en <b></b> milisegundos.',
                timer: 2000,
                timerProgressBar: true,
                onBeforeOpen: () => {
                    Swal.showLoading()
                    timerInterval = setInterval(() => {
                        const content = Swal.getContent()
                        if (content) {
                            const b = content.querySelector('b')
                            if (b) {
                                b.textContent = Swal.getTimerLeft()
                            }
                        }
                    }, 100)
                },
                onClose: () => {
                    clearInterval(timerInterval)
                }
            }).then((result) => {
                /* Read more about handling dismissals below */
                if (result.dismiss === Swal.DismissReason.timer) {
                    $.ajax({
                        type: "GET",
                        url: `http://127.0.0.1:8000/iglesia/eliminar/${id}`,

                        dataType: "json",
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
                        },
                        success: (resp) => {
                            if (resp.existe) {
                                swalWithBootstrapButtons.fire(
                                    'Eliminado!',
                                    resp.message,
                                    'success'
                                )
                                table.ajax.reload();
                            }
                        }
                    });

                }
            })

        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'Tu registro está seguro :)',
                'error'
            )
        }
    })
}