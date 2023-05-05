

function filterProduct(name){
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let buttons = document.querySelectorAll(".button-value");
    code = '';
    buttons.forEach((button) => {
    //check if value equals innerText
        if (name.toUpperCase() === button.innerText.toUpperCase()) {
          if (button.classList.contains("active")) {
            button.classList.remove("active");
          } else {
            button.classList.add("active");
            code += button.innerText.toLowerCase() + ',';
          }
        } else {
            if (button.classList.contains("active")) {
                code += button.innerText.toLowerCase() + ',';
            }
        }
    });
    console.log(code);
    var data;
    $.ajax({
          url: '/api/filter_selector',
          type: 'POST',
          data: {'my_data': code, 'csrfmiddlewaretoken': csrfToken},
          success: function(response) {
            data = response.data;
              console.log("success in js");
              updateContainer(data);
          }
        });
}
function updateContainer(data){
    const container = document.getElementById('allindi');
    container.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
        container.innerHTML += `
           <button type="button" class="container indi" data-toggle="modal" data-target="#${data[i].name}">
              <p class="text-center">${data[i].name}</p>
            </button>
            <div class="modal fade" id=${data[i].name} tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">${data[i].name}</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <p>Account Name: ${data[i].accountName}</p>
                        <ul>
                            <li>Account Type: <span>${data[i].accountType}</span></li>
                            <li>Level of Influence: <span>${data[i].level}</span></li>
                            <li>Audience Country: <span>${data[i].audience}</span></li>
                            <li>Followers: <span>${data[i].followers}</span></li>
                            <li>Viewers: <span>${data[i].viewers}</span></li>
                            <li>Comments: <span>${data[i].comments}</span></li>
                            <li>Likes: <span>${data[i].likes}</span></li>
                        </ul>
                      </div>
                    </div>
                </div>
            </div>
        `;
    }
}
