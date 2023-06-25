
$(document).ready(function() {
  $.ajax({ 
      type: 'GET', 
      url: 'json/dataset.json',
      data: { get_param: 'value' }, 
      dataType: 'json',
      success: function (data) { 
        //console.log(data);
        let source = document.querySelector('#handlebarScript').html;
        let templateScript = Handlebars.compile(source); // returns a function
        var contentToLoad = document.getElementById("datasets")
        contentToLoad.innerHTML = templateScript(data);
      }
  });
});
