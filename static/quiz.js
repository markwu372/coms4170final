function check(choice) {
    let created = {
        "correct": true,
        "topic": quiz_data['answer']
    };

    if (choice==quiz_data['answer']) {
        $("#" + quiz_data['answer']).addClass('correct');
    }
    else {
        created['correct'] = false;
        $("#" + choice).addClass('wrong');
        $("#" + quiz_data['answer']).addClass('correct');
    }

    //for correct answers, increase the correct_answer variable in server.py; otherwise, add to recommended_list
    //   $.ajax({
    //         type: "POST",
    //         url: "quiz/correct",
    //         dataType : "json",
    //         contentType: "application/json; charset=utf-8",
    //         data : JSON.stringify(created),
    //         success: function(){
    //
    //         },
    //         error: function(request, status, error){
    //             console.log("Error");
    //             console.log(request);
    //             console.log(status);
    //             console.log(error);
    //         }
    //   });
}

$(document).ready(function(){
    $("#show_hint").click(function(event){
        $(".question").empty();
        let sol_img = quiz_data['solution'];
        let hint = $("<img src=" + sol_img + " alt='hint_img'> </img>");
        $(".question").append(hint);
    });

    // $("#show_answer").click(function(){
    //     let choice = document.quizzes.q.value;
    //     console.log(choice);
    //     if (choice==quiz_data['answer']) {
    //         count += 1
    //     }
    //     console.log(count);
    //     console.log(quiz_data['answer']);
    //     $("#" + choice).addClass('wrong');
    //     $("#" + quiz_data['answer']).addClass('correct');
    // });

    $(".next_btn").click(function(){
        if (quiz_data["quiz_id"] < 5){
            window.location.replace('/quiz/' + quiz_data["next_lesson"]);
        }
        else{
            window.location.replace('/report');
        }
    });
});