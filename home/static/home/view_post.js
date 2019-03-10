function show_comment_form(node){
	$(node).siblings("#comment_comment_form").find("form").css('display', 'block');
}

function hide_comment_form(node){
	$(node).css('display', 'none');
}