let table = '';
let Users = new Object();
let enviar = document.querySelector('.enviar');
let editarTados = []

enviar.addEventListener("click", (e) => {
    e.preventDefault();

    const form = document.querySelector('form');

    $.ajax({
        method: form.method,
        url: form.action,
        dataType: "JSON",
        data: new FormData(form),
        processData: false,
        contentType: false,
        success: (resp) => {

            Toast.fire({
                icon: resp.estado,
                title: resp.message
            });
            if (resp.estado === 'success') {
                form.reset();

            }
            setTimeout(() => {
                table.ajax.reload();
            }, 3000);
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
        toast.addEventListener('mouseenter', Swal.stopTimer);
        toast.addEventListener('mouseleave', Swal.resumeTimer);
    }
});


const getUsers = () => {

    table = $('#listaTable').DataTable({
        "processing": true,
        "ajax": 'http://127.0.0.1:8000/users/exploradores-listado',
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
        },
        "columns": [
            { "title": "Nombre", "data": "nombre" },
            { "title": "Apellidos", "data": "apellidos" },
            { "title": "Identificacion", "data": "identificacion" },
            { "title": "Dirección", "data": "direccion" },
            { "title": "Teléfono", "data": "telefono" },

            {
                title: "Acción",
                width: "30%",
                data: null,
                render: function(data, type, row, meta) {
                    editarTados.push(row)
                    return "<a  href='#' onclick=getEditar(" + row.pk + ") class='btn btn-warning btn-sm' data-toggle='modal' data-target='#myModal' data-backdrop='static' data-keyboard='false'><i class='fa fa-edit'></i> Editar</a>   <a href='#' class='btn btn-danger btn-sm eliminar' onclick=getEliminar(" + row.pk + ") ><i class='fa fa-trash'></i> Eliminar</a>";
                }
            }
        ],
    });
};
getUsers();

getEliminar = (id) => {

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    });

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
            let timerInterval;
            Swal.fire({
                title: 'Alerta de cierre automático!',
                html: 'Voy a cerrar en <b></b> milisegundos.',
                timer: 2000,
                timerProgressBar: true,
                onBeforeOpen: () => {
                    Swal.showLoading();
                    timerInterval = setInterval(() => {
                        const content = Swal.getContent();
                        if (content) {
                            const b = content.querySelector('b');
                            if (b) {
                                b.textContent = Swal.getTimerLeft();
                            }
                        }
                    }, 100);
                },
                onClose: () => {
                    clearInterval(timerInterval)
                }
            }).then((result) => {
                /* Read more about handling dismissals below */
                if (result.dismiss === Swal.DismissReason.timer) {
                    $.ajax({
                        type: "GET",
                        url: `http://127.0.0.1:8000/grupos/eliminar-grupo/${id}`,

                        dataType: "json",
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
                        },
                        success: (resp) => {


                            swalWithBootstrapButtons.fire(
                                'Eliminado!',
                                resp.message,
                                resp.estado
                            );
                            table.ajax.reload();

                        }
                    });
                }
            });

        } else if (result.dismiss === Swal.DismissReason.cancel) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'Tu registro está seguro :)',
                'error'
            );
        }
    });
};

getEditar = (id) => {
    Users.pk = id
    let editar = editarTados.filter(x => x.pk === id)[0];
    let form = document.querySelector('form');
    form.action = '/grupos/editar-grupo/' + id;
    $('input[name="nombre"]').val(editar.nombre).trigger('change');
};


Cerrar = () => {
    const form = document.querySelector('form');
    form.reset();
}
