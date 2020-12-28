let table = '';
let editarTados = []
let Destacamento = new Object();
let enviar = document.querySelector('.destacamento-enviar');

Cerrar = () => {
    const form = document.querySelector('form');
    form.reset();
}
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
            if (resp.existe) {

                Toast.fire({
                    icon: resp.estado,
                    title: resp.message
                });
                if (resp.estado === 'success') {
                    if (Destacamento.pk == 0) {
                        form.reset();
                    }
                }
                setTimeout(() => {
                    table.ajax.reload();
                }, 3000);
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
        toast.addEventListener('mouseenter', Swal.stopTimer);
        toast.addEventListener('mouseleave', Swal.resumeTimer);
    }
});


const getDestacamento = () => {

    table = $('#listaTable').DataTable({
        "processing": true,
        "ajax": 'http://127.0.0.1:8000/destacamento/lista-destacamento',

        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
        },
        "columns": [{
                title: "Foto",
                width: "5%",
                data: null,
                render: function(data, type, row, meta) {
                    return "<img class='user-avatar rounded-circle' src='/media/" + (row.imagen === null || row.imagen === "" ? '400px-Face-smile.svg.png' : row.imagen) + "' alt='" + row.nombre + "' style='height:50px'>";
                }
            },
            { "title": "Destacamento", "data": "nombre" },
            { "title": "Iglesia", "data": "iglesia" },
            { "title": "Número", "data": "numero" },
            { "title": "Distrito", "data": "distrito" },
            { "title": "Sección", "data": "seccion" },
            {
                title: "Acción",
                width: "32%",
                data: null,
                render: function(data, type, row, meta) {
                
                    editarTados.push(row)
                    return "<a href='/destacamento/detalle-destacamento/" + row.destacamento_id + "' class='btn btn-info btn-sm'><i class='fa fa-list'></i> Detalle</a>    <a  onclick=getEditar(" + row.destacamento_id + ") class='btn btn-warning btn-sm' data-toggle='modal' data-target='#myModal' data-backdrop='static' data-keyboard='false'><i class='fa fa-edit'></i> Editar</a>   <a href='#' class='btn btn-danger btn-sm eliminar' onclick=getEliminar(" + row.destacamento_id + ") ><i class='fa fa-trash'></i> Eliminar</a>";
                }
            }
        ],
    });
};
getDestacamento();
getEditar = (id) => {
  
    Destacamento.pk = id
    let editar = editarTados.filter(x => x.destacamento_id === id)[0];

    let form = document.querySelector('form');
    form.action = '/destacamento/editar-destacamento/' + id;
    $('input[name="nombre"]').val(editar.nombre).trigger('change');
    $('input[name="distrito"]').val(editar.distrito).trigger('change');
    $('input[name="numero"]').val(editar.numero).trigger('change');
    $('input[name="pk"]').val(editar.destacamento_id).trigger('change');
    $('#igelsia_id').val(editar.iglesia_id).trigger('change');
    $('#seccion_id').val(editar.seccion_id).trigger('change');
    editarTados=[]
};
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
                        url: `http://127.0.0.1:8000/destacamento/eliminar-destacamento/${id}`,

                        dataType: "json",
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
                        },
                        success: (resp) => {
                            if (resp.existe) {
                                table.ajax.reload();
                            }
                            swalWithBootstrapButtons.fire(
                                'Eliminado!',
                                resp.message,
                                resp.estado
                            );

                        },
                        error: (resp)=>{
                            swalWithBootstrapButtons.fire(
                                'No se puede eliminar',
                                resp.statusText,
                                'error'
                            );
                        }
                    });

                }
            });

        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'Tu registro está seguro :)',
                'error'
            );
        }
    });
};