window.onload =function(){
    counter = 0;
    document.getElementById("add-button").onclick = function() {
        counter++;
        var objTo = document.getElementById('myForm');
        var divtest = document.createElement("div");
        divtest.innerHTML = '<p><label for="id_data">Data'+counter+'</label><input id="id_data" max_length="255" ' +
            'name="data'+counter+'" type="text" required>';

        objTo.append(divtest);
        $("[name=extra_field_count]").val(counter);
    }
    document.getElementById("submit-button").onclick = function () {
        document.getElementById("myForm").submit()
    }
}