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

function showEditItemForm(item) {
   card_form = $('#card' + item);
   edit_form = $('#editItemForm' + item);
   edit_form.find('input[name=item]').val(card_form.find('input[name=item]').val())
   edit_form.find('textarea[name=comment]').val(card_form.find('input[name=comment]').val())
   $('#card' + item).attr('hidden', true);
   $('#editItemForm' + item).attr('hidden', false);
}

function closeEditItemForm(item) {
   $('#card' + item).attr('hidden', false);
   $('#editItemForm' + item).attr('hidden', true);
}
