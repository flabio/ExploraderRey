let enviar = document.querySelector('.enviar');
let editarTados = []
let table = '';
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
                icon: resp.estado,
                text: resp.message,
            })
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
    console.log(id);
    $.ajax({
        type: "GET",
        url: `http://127.0.0.1:8000/destacamento/lista-destacamento`,
        success: (resp) => {
            let opt = "";
            let datos = resp.data.filter(x => x.iglesia_id == id);
            for (item of datos) {
                opt += "<option value=" + item.destacamento_id + ">" + item.nombre + "</option>";
            }
            document.querySelector('.destacamento').innerHTML = opt;
        }
    });
}