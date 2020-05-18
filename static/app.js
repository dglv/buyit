function copyToClipboard() {
    var dummy = document.createElement('input'),
    text = window.location.href;
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    dummy.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand('copy');
    document.body.removeChild(dummy);
    return false;
}

function showEditItemForm(item_id) {
   card_form = $('#card' + item_id);
   edit_form = $('#editItemForm' + item_id);
   edit_form.find('input[name=item_id]').val(card_form.find('input[name=item_id]').val())
   edit_form.find('input[name=name]').val(card_form.find('input[name=name]').val())
   edit_form.find('textarea[name=comment]').val(card_form.find('input[name=comment]').val())
   $('#card' + item_id).attr('hidden', true);
   $('#editItemForm' + item_id).attr('hidden', false);
}

function closeEditItemForm(item_id) {
   $('#card' + item_id).attr('hidden', false);
   $('#editItemForm' + item_id).attr('hidden', true);
}
