function check(choice) {
    let created;
    let rules = ["frames", "rule_of_thirds", "diagonals", "leading_lines", "balance"]
    $("#feedback").empty()
    let feedback = "feedback: <br>" 
    if (choice==quiz_data['answer']) {
        created = {
            "correct": '1',
            "topic": quiz_data['answer']
        };
        $("#" + quiz_data['answer']).addClass('correct');
        feedback += "Great Job!"
    }
    else {
        created = {
            "correct": '0',
            "topic": quiz_data['topic']
        };
        $(".question").empty();
        let sol_img = quiz_data['solution'];
        let hint = $("<img src=" + sol_img + " alt='hint_img'> </img>");
        $("#" + quiz_data['answer']).removeClass("correct")
        for (let i = 0; i < rules.length; i++) {
            $("#" + rules[i]).removeClass('wrong');
        }
        $(".question").append(hint);
        $("#" + choice).addClass('wrong');
        $("#" + quiz_data['answer']).addClass('correct');
        feedback += "As the annotation suggested, the correct anwser should be <b> " + quiz_data['answer'] + "</b>. ";
        feedback += "Let's review the definition and examples of " + "<a href=\"" + quiz_data['learning_url'] + "\">" + quiz_data['answer'] + ".</a>"
    }
    $("#feedback").append(feedback)
    //for correct answers, increase the correct_answer variable in server.py; otherwise, add to recommended_list
    $.ajax({
        type: "POST",
        url: "/quiz/correct",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(created),
        success: function(item){

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

$(document).ready(function(){
    $("#show_hint").click(function(event){
        $(".question").empty();
        let sol_img = quiz_data['solution'];
        let hint = $("<img src=" + sol_img + " alt='hint_img'> </img>");
        $(".question").append(hint);
    });

    $("#show_answer").click(function(){
        $(this).prop('disabled', true); 
        // let choice = document.quizzes.q.value;
        // console.log(choice);
        // if (choice==quiz_data['answer']) {
        //     count += 1
        // }
        // console.log(count);
        // console.log(quiz_data['answer']);
        // $("#" + choice).addClass('wrong');
        // $("#" + quiz_data['answer']).addClass('correct');
    });

    $(".next_btn").click(function(){
        if (quiz_data["quiz_id"] < 6){
            window.location.replace('/quiz/' + quiz_data["next_lesson"]);
        }
        else{
            window.location.replace('/report');
        }
    });

    $(".animated-progress span").each(function () {
        $(this).animate(
          {
            width: $(this).attr("data-progress") + "%",
          },
          500
        );
        
      });
});