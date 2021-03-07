

function empty_modal() {
    // for creating a new object.
    $('#modal_sm_create').val() == '';
}

function create() {
    // create object by AJAX.
    let surgery_method = $('#modal_sm_create').val();
    // console.log('surgery_method', surgery_method);

    if (surgery_method === '' || surgery_method === 'undefined') {
        $('#ModalFailure').modal();
        $('#failure_message').text('資料不能為空');
        return;
    }

    axios.post('/surgery_method_create/', {
        params: {
            surgery_method: surgery_method,
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
    $('#modal_sm_update').val(obj);
    $('#modal_sm_update').attr('name', id);
}

function update() {
    // update object by AJAX.
    let id = $('#modal_sm_update').attr('name');
    let surgery_method = $('#modal_sm_update').val();

    axios.post('/surgery_method_update/', {
        params: {
            id: id,
            surgery_method: surgery_method,
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

    axios.post('/surgery_method_delete/', {
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






