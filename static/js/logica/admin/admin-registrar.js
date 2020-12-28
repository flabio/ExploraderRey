let enviar = document.querySelector('.enviar');

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
            Swal.fire({
                title: resp.estado === 'success' ? '' : resp.title,
                icon: resp.estado,
                text: resp.message,
            });

            if (resp.estado === 'success') {
                if (document.querySelector('#data-id').value === '' || document.querySelector('#data-id').value === null) {
                    form.reset();
                }
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


traerDestacamento = (id) => {

    let destacamento_id = document.querySelector('.destacamento').getAttribute('data-id');
    $.ajax({
        type: "GET",
        url: `http://127.0.0.1:8000/destacamento/lista-destacamento`,
        success: (resp) => {
            let opt = "";
            let datos = resp.data.filter(x => x.iglesia_id == id);
            for (item of datos) {
                if (parseInt(destacamento_id) === item.pk) {
                    opt += "<option value=" + item.destacamento_id + " selected >" + item.nombre + "</option>";
                } else {
                    opt += "<option value=" + item.destacamento_id + ">" + item.nombre + "</option>";
                }
            }
            document.querySelector('.destacamento').innerHTML = opt;

        }
    });
};
