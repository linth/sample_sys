

function empty_modal() {
    // for creating a new object.
    $('#modal_ct_create').val() == '';
}

function create() {
    // create object by AJAX.
    let cancer_type = $('#modal_ct_create').val();
    // console.log('cancer_type', cancer_type);

    if (cancer_type === '' || cancer_type === 'undefined') {
        $('#ModalFailure').modal();
        $('#failure_message').text('資料不能為空');
        return;
    }

    axios.post('/cancer_type_create/', {
        params: {
            cancer_type: cancer_type,
        }
    })
    .then(function(response) {
        // console.warn('response', response.data);

        if (response.data['result'] === 'successful') {
            $('#ModalSuccessful').modal();
            $('#successful_message').text(response.data['message']);
        } else if (response.data['result'] === 'failure') {
            $('#ModalFailure').modal();
            $('#failure_message').text(response.data['message']);
        }
    })
    .catch(function(error) {
        //console.log('error', error);
        $('#ModalFailure').modal();
        $('#failure_message').text(error);
    })
}

function get_object(id, obj) {
    // get object and render them on modal.
    $('#modal_ct_update').val(obj);
    $('#modal_ct_update').attr('name', id);
}

function update() {
    // update object by AJAX.
    let id = $('#modal_ct_update').attr('name');
    let cancer_type = $('#modal_ct_update').val();

    axios.post('/cancer_type_update/', {
        params: {
            id: id,
            cancer_type: cancer_type,
        }
    })
    .then(function(response) {
        //console.log('response', response.data);
        if (response.data['result'] === 'successful') {
            $('#ModalSuccessful').modal();
            $('#successful_message').text(response.data['message']);
        } else if (response.data['result'] === 'failure') {
            $('#ModalFailure').modal();
            $('#failure_message').text(response.data['message']);
        }
        //window.location.reload();
    })
    .catch(function(error) {
        //console.log('error', error);
        $('#ModalFailure').modal();
        $('#failure_message').text(error);
    })
}

function get_deleted_object(id) {
    // get object and insert the value of name on modal.
    $('#delete_obj_id').attr('name', id);
}

function delete_obj() {
    // delete object by AJAX.
    let id = $('#delete_obj_id').attr('name');

    axios.post('/cancer_type_delete/', {
        params: {
            id: id,
        }
    })
    .then(function(response) {
        //console.log('response', response.data);
        if(response.data['result'] === 'successful') {
            $('#ModalSuccessful').modal();
            $('#successful_message').text(response.data['message']);
        } else if (response.data['result'] === 'failure') {
            $('#ModalFailure').modal();
            $('#failure_message').text(response.data['message']);
        }
    })
    .catch(function(error) {
        //console.log('error', error);
        $('#ModalFailure').modal();
        $('#failure_message').text(error);
    })
}






