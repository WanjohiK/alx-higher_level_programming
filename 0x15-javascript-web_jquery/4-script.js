// Add a click event listener to the DIV#toggle_header element
  $("div#toggle_header").click(function () {    
    // Check the current class of the <header> element
    if ($'header').hasClass("red")) {
      // If it has the class "red," toggle to "green"
      ($'header').removeClass("red").addClass("green");
    } else if ('header').hasClass("green")) {
      // If it has the class "green," toggle to "red"
      ($'header').removeClass("green").addClass("red");
    } else {
      // If it has no class, add the "red" class
      ($'header').addClass("red");
    }
  });
});
