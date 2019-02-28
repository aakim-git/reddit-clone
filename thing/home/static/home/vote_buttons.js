var black = "rgb(33, 37, 41)";
var grey = "rgb(225,225,225)";
var white = "rgb(255, 255, 255)";
var down = "rgb(65, 89, 244)";
var up = "rgb(244, 140, 66)";
var post_vote_url = "http://127.0.0.1:8000/home/post_vote/";

function increment(post_id, cur_user) {
    $.ajax(
    {
        type: "POST",
        url: post_vote_url,
        data: {
            id: post_id,
            cur_user: cur_user,
            change: "1",
            csrfmiddlewaretoken: getCookie('csrftoken'),
        },

    })
}

function decrement(post_id, cur_user) {
    $.ajax(
    {
        type: "POST",
        url: post_vote_url,
        data: {
            id: post_id,
            cur_user: cur_user,
            change: "-1",
            csrfmiddlewaretoken: getCookie('csrftoken'),
        },

    })
}

function update_vote(buttons, vote) {
    if (vote == 1) {
        $(buttons).find(".upvote").css({ "color": up, "background-color": white });
    }
    else if (vote == -1) {
        $(buttons).find(".downvote").css({ "color": down, "background-color": white });
    }
}




function upvote(buttons, post_id, cur_user) {
    if (cur_user == 0) {
        alert("You need to login to vote!");
        return;
    }

    cur_rank = Number($(buttons).parent().find(".rank").children().text());
    if ($(buttons).find(".upvote").css("color") == black) {
        $(buttons).find(".upvote").css({ "color": up, "background-color": white });
        increment(post_id, cur_user);
        cur_rank = cur_rank + 1;

        if ($(buttons).find(".downvote").css("color") == down) {
            $(buttons).find(".downvote").css({ "color": black, "background-color": grey });
            increment(post_id, cur_user);
            cur_rank = cur_rank + 1;
        }
        $(buttons).parent().find(".rank").children().text(cur_rank);
    }

    else {
        $(buttons).find(".upvote").css({ "color": black, "background-color": grey });
        $(buttons).parent().find(".rank").children().text(cur_rank - 1);
        decrement(post_id, cur_user);
    }
}

function downvote(buttons, post_id, cur_user) {
    if (cur_user == 0) {
        alert("You need to login to vote!");
        return;
    }

    cur_rank = Number($(buttons).parent().find(".rank").children().text());
    if ($(buttons).find(".downvote").css("color") == black) {
        $(buttons).find(".downvote").css({ "color": down, "background-color": white });
        decrement(post_id, cur_user);
        cur_rank = cur_rank - 1;

        if ($(buttons).find(".upvote").css("color") == up) {
            $(buttons).find(".upvote").css({ "color": black, "background-color": grey });
            decrement(post_id, cur_user);
            cur_rank = cur_rank - 1;
        }
        $(buttons).parent().find(".rank").children().text(cur_rank);
    }

    else {
        $(buttons).find(".downvote").css({ "color": black, "background-color": grey });
        $(buttons).parent().find(".rank").children().text(cur_rank + 1);
        increment(post_id, cur_user);
    }
}

