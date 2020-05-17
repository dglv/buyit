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

function showEditItemModal(item, commentary) {
   $('#editModalItem').val(item)
   $('#editModalCommentary').val(commentary);
   $('#editModal').modal('show');
}