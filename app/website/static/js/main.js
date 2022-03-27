$(document).ready(function(){ 
    $(".pa_teams").hide(); //Hides anything with the "pa_teams" CSS class
    $(".pa_individuals").hide(); //Hides anything with the "pa_individuals" CSS class
    $(".le_teams").hide(); //Hides anything with the "le_teams" CSS class
    $(".le_individuals").hide(); //Hides anything with the "le_individuals" CSS class
    $(".ev_individuals").hide(); //Hides anything with the "ev_individuals" CSS class
    $(".ev_teams").hide(); //Hides anything with the "ev_teams" CSS class
    $("#select_participants").change(function(){ //If the value of the select menu with ID select_participants changes
        var value = $(this).find("option:selected").val() //assign the new value to the variable "value"
        if(value == "pa_individuals"){ //if the selected value is "pa_individuals"
            console.log("hi")
            $(".pa_teams").hide(); //Hide anything with the "pa_teams" CSS class
            $(".pa_individuals").show() //Show anything with the "pa_individuals" CSS class
            if (document.getElementById("team-view").classList.contains("team-view-new")) { //If an element with ID "team-view" has the "team-view-new" CSS class
                document.getElementById("team-view").classList.remove("team-view-new"); //Remove the "team-view-new" CSS class from elements with "team-view" ID
                document.getElementById("team-view").classList.add("team-view"); //Add the "team-view" CSS class from elements with "team-view" ID
            }
            if (document.getElementById("initial-view").classList.contains("initial-view")) { //If an element with ID "initial-view" has the "initial-view" CSS class
                document.getElementById("initial-view").classList.remove("initial-view"); //Remove the "initial-view" CSS class from elements with "initial-view" ID
                document.getElementById("initial-view").classList.add("initial-view-new"); //Add the "initial-view-new" CSS class from elements with "initial-view" ID
            }
            document.getElementById("individual-view").classList.remove("individual-view"); //Remove the "individual-view" CSS class from elements with "individual-view" ID
            document.getElementById("individual-view").classList.add("individual-view-new"); //Add the "individual-view-new" CSS class from elements with "individual-view" ID
        }
        else if(value == "pa_teams"){ //if the selected value is "pa_teams"
            $(".pa_individuals").hide(); //Hide anything with the "pa_individuals" CSS class
            $(".pa_teams").show() //Show anything with the "pa_teams" CSS class
            if (document.getElementById("individual-view").classList.contains("individual-view-new")) { //If an element with ID "tindividual-view" has the "individual-view-new" CSS class
                document.getElementById("individual-view").classList.remove("individual-view-new"); //Remove the "individual-view-new" CSS class from elements with "individual-view" ID
                document.getElementById("individual-view").classList.add("individual-view"); //Add the "individual-view" CSS class from elements with "individual-view" ID
            }
            if (document.getElementById("initial-view").classList.contains("initial-view")) { //If an element with ID "initial-view" has the "initial-view" CSS class
                document.getElementById("initial-view").classList.remove("initial-view"); //Remove the "initial-view" CSS class from elements with "initial-view" ID
                document.getElementById("initial-view").classList.add("initial-view-new"); //Add the "initial-view-new" CSS class from elements with "initial-view" ID
            }
            document.getElementById("team-view").classList.remove("team-view"); //Remove the "team-view" CSS class from elements with "team-view" ID
            document.getElementById("team-view").classList.add("team-view-new"); //Add the "team-view-new" CSS class from elements with "team-view" ID
        }
    })
    $("#select_leaderboard").change(function(){ //If the value of the select menu with ID select_leaderboard changes
        var value = $(this).find("option:selected").val() //assign the new value to the variable "value"
        if(value == "le_individuals"){ //if the selected value is "le_individuals"
            $(".le_teams").hide(); //Hide anything with the "le_teams" CSS class
            $("#leaderboard-initial").hide(); //Hide anything with the "leaderboard-initial" CSS class
            $(".le_individuals").show() //Show anything with the "le_individuals" CSS class
        }
        else if(value == "le_teams"){ //if the selected value is "le_individuals"
            $(".le_individuals").hide(); //Hide anything with the "le_individuals" CSS class
            $("#leaderboard-initial").hide(); //Hide anything with the "leaderboard-initial" CSS class
            $(".le_teams").show() //Show anything with the "le_teams" CSS class
        }
    })
    $("#select_event").change(function(){ //If the value of the select menu with ID select_leaderboard changes
        var value = $(this).find("option:selected").val() //assign the new value to the variable "value"
        console.log(value)
        if(value == "ev_individuals"){ //if the selected value is "ev_individuals"
            $("#events-initial").hide();
            $(".ev_teams").hide(); //Hide anything with the "ev_teams" CSS class
            $("#events-initial").hide(); //Hide anything with the "events-initial" CSS class
            $(".ev_individuals").show() //Show anything with the "ev_individuals" CSS class
        }
        else if(value == "ev_teams"){ //if the selected value is "ev_individuals"
            $("#events-initial").hide();
            $(".ev_individuals").hide(); //Hide anything with the "ev_individuals" CSS class
            $("#events-initial").hide(); //Hide anything with the "events-initial" CSS class
            $(".ev_teams").show() //Show anything with the "ev_teams" CSS class
        }
    })
})

function showPassword() {
    var inputBox = document.getElementById("passwordEntry");
    if (inputBox.type == "password") {
        inputBox.type = "text";
    } else {
        inputBox.type = "password";
    }
}