$(document).ready(function(){
    description = homepage_data["description"]
    rules = homepage_data["rules"]
    $("#description").append(description)
    rules_str = "<ul>"
    for (let i = 0; i < rules.length; i++) {
        rules_str += "<li>" + rules[i] + "</li>"
    }
    rules_str += "</li>"
    console.log(rules_str)
    $("#rules").append(rules_str)
})