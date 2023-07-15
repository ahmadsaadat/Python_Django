

function searchByDescription() {

    let input = document.getElementById('description-search');
    let filter = input.value.toLowerCase();
    let table = document.getElementById('product-table');
    let tr = table.getElementsByTagName('tr');
    for (i = 1; i < tr.length; i++) {
        let td = tr[i].getElementsByClassName('product-description')[0];
        if (td) {
            let txtValue = td.textContent || td.innerText;
            txtValue = txtValue.toLowerCase()
            if (txtValue.includes(filter)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function filterByCategory(){

    let checkboxes = document.getElementsByClassName('category-checkbox');
    let checkedCategories = [];

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkedCategories.push(checkboxes[i].value);
        }
    }

    table = document.getElementById('product-table');
    tr = table.getElementsByTagName('tr');
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByClassName('product-category')[0];
        if(!checkedCategories.includes(td.innerText)){
            tr[i].style.display="none"
        } else {
            tr[i].style.display=""
        }
    }
}

function filterByTags(){

    let checkboxes = document.getElementsByClassName('tag-checkbox');
    let checkedCategories = [];

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkedCategories.push(checkboxes[i].value);
        }
    }

    table = document.getElementById('product-table');
    tr = table.getElementsByTagName('tr');
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByClassName('product-tags')[0];
        let dataTags = td.innerText.trim().split(',')

        for(let dataTag of dataTags){
            if(!checkedCategories.includes(dataTag.trim())){
                tr[i].style.display="none"
            } else {
                tr[i].style.display=""
            }
        }
    }
}