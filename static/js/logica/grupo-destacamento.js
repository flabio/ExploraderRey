let table = '';
let enviar = document.querySelector('.grupo-destacamento-enviar');


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
               
                setTimeout(() => {
                    table.ajax.reload();
                }, 3000);
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
                        url: `http://127.0.0.1:8000/destacamento/eliminar-grupo-destacamento/${id}`,

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
                                );
                                table.ajax.reload();
                            }
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