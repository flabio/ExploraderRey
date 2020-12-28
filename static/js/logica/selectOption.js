iglesia=[];
destacamento = [];
grupo =[];

(ListadoIglesia = () => {
    $.ajax({
        method: 'GET',
        url: '../iglesia/lista-iglesia',
        success: (resp) => {
            iglesia.push(resp.data)
            let opt = "";
            opt = "<option value=0>[Seleccione el iglesia]</option>";
            for (item of resp.data) {
                opt += "<option value=" + item.iglesia_id + ">" + item.nombre + "</option>";
            }
            document.querySelector('.iglesia').innerHTML = opt
        }
    })
})();
traerDestacamento = (id) => {

    let destacamento_id = document.querySelector('.destacamento').getAttribute('data-id');
    $.ajax({
        type: "GET",
        url: `../destacamento/lista-destacamento`,
        success: (resp) => {
             let opt = "";
            let datos = resp.data.filter(x => x.iglesia_id == id);
            opt = "<option value=0>[Seleccione el destacamento]</option>";
            for (item of datos) {
                if (parseInt(destacamento_id) === item.destacamento_id) {
                    opt += "<option value=" + item.destacamento_id + " selected >" + item.nombre + "</option>";
                } else {
                    opt += "<option value=" + item.destacamento_id + ">" + item.nombre + "</option>";
                }
            }
            document.querySelector('.destacamento').innerHTML = opt;

        }
    });
};

ListadoGrupo = (id) => {
    
    $.ajax({
        method: 'GET',
        url: '../destacamento/lista-grupo-destacamento/'+id,
        success: (resp) => {
            
            let opt = "";
            opt = "<option value=0>[Seleccione el grupo]</option>";
            for (item of resp.data) {
                    opt += "<option value=" + item.grupo_id + "  >" + item.nombre + "</option>";
            }
            document.querySelector('.grupos').innerHTML = opt
        }
    })
};

ListadoGrupoEditar = (id) => {
 resulta_grupo=[];
    $.ajax({
        type: "GET",
        url: `../destacamento/lista-destacamento`,
        success: (resp) => {
            console.log('destacamento----')
            console.log(resp.data)
         

        }
    });


    $.ajax({
        method: 'GET',
        url: '../destacamento/lista-grupo-destacamento/'+0,
        success: (resp) => {
            console.log('grupo----')
            console.log(resp.data)
            result= resp.data.filter(x=>x.grupo_id==id);
            console.log(result)
            
        }
    })



};