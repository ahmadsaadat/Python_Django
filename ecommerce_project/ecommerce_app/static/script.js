function searchByDescription() {
    const input = document.getElementById('description-search');
    const filter = input.value.toLowerCase();
    const table = document.getElementById('product-table');
    const rows = table.getElementsByTagName('tr');
  
    for (let i = 1; i < rows.length; i++) {
        let td = rows[i].getElementsByClassName('product-description')[0];
        if (td) {
            let txtValue = td.textContent || td.innerText;
            txtValue = txtValue.toLowerCase()
            rows[i].style.display = txtValue.includes(filter) ? "" : "none";
        }
    }
}

function filterByCategory() {
    const checkboxes = document.getElementsByClassName('category-checkbox');
    const checkedCategories = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.value);
    const table = document.getElementById('product-table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const td = rows[i].getElementsByClassName('product-category')[0];
        rows[i].style.display = checkedCategories.includes(td.innerText) ? "" : "none";
    }
}

function filterByTags() {
    const checkboxes = document.getElementsByClassName('tag-checkbox');
    const checkedTags = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.value);
    const table = document.getElementById('product-table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const td = rows[i].getElementsByClassName('product-tags')[0];
        const dataTags = td.innerText.trim().split(',');

        for(let dataTag of dataTags){
            rows[i].style.display = checkedTags.includes(dataTag.trim()) ? "" : "none";
        }
    }
}
