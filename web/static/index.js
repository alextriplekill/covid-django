$(document).ready(function(){
	$.getJSON('static/ru.json').done(function(data){
  $($('body > div > div > div > div > table > tbody')[0].children).each(function () {
    let value = $(this)[0].children[0].innerHTML;
	  $(this)[0].children[0].innerHTML = data[value.trim()] + ' ';
  });
        $($('body > div > div > div > div > table > thead > tr')[0].children).each(function () {
            let value = $(this)[0].innerHTML;
            $(this)[0].innerHTML = data[value.trim()] + ' ';
        });

  $('.dataframe').DataTable({
      paging: true,
  })
})
})