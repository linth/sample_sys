

function empty_modal() {
    // for creating a new object.
    $('#modal_med_create').val() == '';
}

function create() {
    // create object by AJAX.
    let medication = $('#modal_med_create').val();
    // console.log('medication', medication);

    if (medication === '' || medication === 'undefined') {
        $('#ModalFailure').modal();
        $('#failure_message').text('資料不能為空');
        return;
    }

    axios.post('/medication_create/', {
        params: {
            medication: medication,
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
    $('#modal_med_update').val(obj);
    $('#modal_med_update').attr('name', id);
}

function update() {
    // update object by AJAX.
    let id = $('#modal_med_update').attr('name');
    let medication = $('#modal_med_update').val();

    axios.post('/medication_update/', {
        params: {
            id: id,
            medication: medication,
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

    axios.post('/medication_delete/', {
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






