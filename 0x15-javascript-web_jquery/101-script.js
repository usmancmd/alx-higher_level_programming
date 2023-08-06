//  Adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function () {
  
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');

    $('UL.my_list').append(newItem);
  });

  $('#remove_item').click(function () {
    $('UL.my_list LI:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
