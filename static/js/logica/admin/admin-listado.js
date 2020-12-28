let table = "";
const getListado = () => {

    table = $('#listaTable').DataTable({
        "processing": true,
        "ajax": 'http://127.0.0.1:8000/administrador/lista-adminjson',
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
        },
        "columns": [{
                "title": "Nombre",
                "data": "nombre"
            }, {
                "title": "Apellidos",
                "data": "apellidos"
            }, {
                "title": "Identificacion",
                "data": "identificacion"
            },
            {
                "title": "Rol",
                "data": "rol"
            },
            {
                title: "Acción",
                width: "22%",
                data: null,
                render: function(data, type, row, meta) {
                    return " <a  href='/administrador/editar/" + row.pk + "' class='btn btn-warning btn-sm'><i class='fa fa-edit'></i> Editar</a>   <a href='#' class='btn btn-danger btn-sm eliminar' onclick=getEliminar(" + row.id + ") ><i class='fa fa-trash'></i> Eliminar</a> ";
                }
            }
        ],
    });
};
getListado();

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
                        url: `http://127.0.0.1:8000/administrador/eliminar/${id}`,

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