

function empty_modal() {
    // for creating a new object.
    $('#no_of_box').val() == '';
    $('#position').val() == '';
}

function create() {
    // create object by AJAX.
    let box = $('#nob').val();
    let position = $('#modal_position_create').val();
    console.log('box', box, 'position', position);

    if (box === '' || box === 'undefined' || position === '' || position === 'undefined') {
        $('#ModalFailure').modal();
        $('#failure_message').text('資料不能為空');
        return;
    }

    axios.post('/box_position_create/', {
        params: {
            box: box,
            position: position,
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

function get_object(id, box, position) {
    // get object and render them on modal.
    $('select#nob').val(box);
    $('#modal_position_update').val(position);
    $('#box_position').attr('name', id);
}

function update() {
    // update object by AJAX.
    let id = $('#box_position').attr('name');
    let box = $('#nob').val();
    let position = $('modal_position_update').val();
    console.log('box', box, 'position', position);

    axios.post('/box_position_update/', {
        params: {
            id: id,
            box: box,
            position: position,
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






