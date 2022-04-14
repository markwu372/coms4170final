$(document).ready(function(){
    description = homepage_data["description"]
    rules = homepage_data["rules"]
    $("#description").append(description)
    rules_str = "<ul>"
    for (let i = 0; i < rules.length; i++) {
        id = i + 1
        rules_str += "<a href=\"" + "lessons/" + id + "\">" + "<li>" + rules[i] + "</li> </a>" 
    }
    rules_str += "</ul>"
    console.log(rules_str)
    $("#rules").append(rules_str)
})