$(document).ready(function() {
    $("#weeklyBtn").click(function() {
        $("#displayActive").text("Weekly Active people");
        $("#daily").slideUp(function() {
            $("#yearly").slideUp(function() {
                $("#weekly").slideDown(1000);
            });
        });
    });
    $("#yearlyBtn").click(function() {
        $("#displayActive").text("Yearly Active people");
        $("#daily").slideUp(function() {
            $("#weekly").slideUp(function() {
                $("#yearly").slideDown(1000);
            });
        });
    });
    $("#dailyBtn").click(function() {
        $("#displayActive").text("Daily Active people");
        $("#yearly").slideUp(function() {
            $("#weekly").slideUp(function() {
                $("#daily").slideDown(1000);
            });
        });
    });
});