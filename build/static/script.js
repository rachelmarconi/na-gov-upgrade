function clickForMore(arrest_list, case_number){
	console.log(case_number)
	/* console.log(arrest_list_j)
	var arrest_list = JSON.parse(arrest_list_j) */
	console.log(arrest_list)
	
	var arrest = [];
	for (x = 0; x<arrest_list.length; x++){
		if (arrest_list[x]['UMPD CASE NUMBER'] == case_number){
			arrest = arrest_list[x]
			break;
		}
	}
	console.log(arrest)
	
	var content = `<h2>Arrest entry:</h2>
		<ul>
			<li>Arrest number: ${ arrest['ARRESTNUMBER'] }</li>
			<li>Charge date and time: ${ arrest['ARRESTED DATE TIMECHARGE'] }</li>
			<li>Age: ${ arrest['AGE'] }</li> <!--always empty :( -->
			<li>Race: ${ arrest['RACE'] }</li>
			<li>Gender: ${ arrest['SEX'] }</li>
			<li>Description: ${ arrest['DESCRIPTION'] }</li>
			
		</ul>`
	
	document.getElementById("more-stuff").innerHTML = content;
}