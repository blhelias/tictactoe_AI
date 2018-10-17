turnNb = 0;

function gridData() {
	var data = new Array();
	var xpos = 1; //starting xpos and ypos at 1 so the stroke will show when we make the grid below
	var ypos = 1;
	var width = 100;
	var height = 100;
    var click = 0;
    var value = 0;
	var count = 0;
	// iterate for rows	
	for (var row = 0; row < 3; row++) {
		data.push( new Array() );

		// iterate for cells/columns inside rows
		for (var column = 0; column < 3; column++) {
			data[row].push({
				id: count,
				x: xpos,
				y: ypos,
				width: width,
				height: height,
                click: click,
                value: value
			})
			count += 1;
			// increment the x position. I.e. move it over by 50 (width variable)
			xpos += width;
		}
		// reset the x position after a row is complete
		xpos = 1;
		// increment the y position for the next row. Move it down 50 (height variable)
		ypos += height;	
	}
	return data;
}
// TODO:
function resetGame(){
	pass;
}

gridData = gridData();	
// I like to log the data to the console for quick debugging
console.log(gridData);

var grid = d3.select("#grid")
	.append("svg")
	.attr("width","301px")
	.attr("height","301px");

var row = grid.selectAll(".row")
	.data(gridData)
	.enter().append("g")
	.attr("class", "row");

var column = row.selectAll(".square")
	.data(function(d) { return d; })
	.enter().append("rect")
	.attr("class","square")
	.attr("x", function(d) { return d.x; })
	.attr("y", function(d) { return d.y; })
	.attr("width", function(d) { return d.width; })
	.attr("height", function(d) { return d.height; })
	.style("fill", "#fff")
	.style("stroke", "#222")
	.on('click', function(d) {
		// check if it player 1 turn
		if (turnNb%2==0) {
			// check number of turns
			if(turnNb>=9){
				// check if the div is empty to display the result
				if ($('#result').is(':empty')){		
					document.querySelector("#result").innerHTML = "<h1> Draw </h1>";
					$("#result").css({"color":"grey",
									"text-align":"center"});
				}
			}
			// check if you click on an empty square
			if(d3.select(this)._groups[0][0].__data__.value==0){
				d3.select(this).style("fill","#2C93E8");
				var posClickX = d3.select(this)._groups[0][0].__data__.x;
				var posClickY = d3.select(this)._groups[0][0].__data__.y;
				
				posClickX = posClickX > 100 ? Math.round(posClickX/100) : 0;
				posClickY = posClickY > 100 ? Math.round(posClickY/100) : 0;

				// update the grid according to player 1 click
				gridData = updateGrid(gridData, posClickY, posClickX, "player1");

				//print player and grid 
				console.log("player1");
				console.log(gridData);

				// after human clicks, send the grid to the backend (POST)
				gridData = sendPostToIA(gridData);
				turnNb++;
			}
		}
	});

// POST request to django backend:
// sends the data into a JSON format
// receives the data as JSON object with:
// * data (updated grid)
// * id (square id of the returned try)
// * status of the game (win, draw, in progress)
function sendPostToIA(data){
	var data = JSON.stringify(data);
	$.ajax({
		url:'sendData/',
		type:'POST',
		data:data,
		success: function(data){
			var response = JSON.parse(data);
			console.log("player2");
			console.log(response.data);
			gridData = updateSVG(response.id, response.status, "red");
		}
	});
	return gridData
}

function updateGrid(data, posx, posy, joueur){
	if (joueur == "player1"){	
		data[posx][posy].value = 1;
	}else{
		data[posx][posy].value = 2;
	}
	// var id = posx * 3 + posy
	return data;
}

function updateSVG(id, status, color){
	var clickX;
	var clickY;

	// if the game is over --> status = 1 (player1) or 2(player2) or -1 (draw)
	// freeze SVG

	// check number of turn
	if(turnNb>=9){
		document.querySelector("#result").innerHTML = "<h1> Draw </h1>";
		$("#result").css({"color":"grey",
						  "text-align":"center"});
	}else{
		if(turnNb%2==1 || status==10 || status==-10){
			turnNb ++;
			grid.selectAll("rect").each(function(d, i){
				if(d.id==id){
					d3.select(this).style("fill", color);
				}
			});
		}
		// TODO: clean this!
		if(id<=2){
			clickX = 0;
			clickY = id;
		}else if (id<=5){
			clickX = 1;
			clickY = id-3;
		}else{
			clickX = 2;
			clickY = id-6;
		}

		gridData = updateGrid(gridData, clickX, clickY, "player2");
		if ($('#result').is(':empty')){		
			if(status==-10){
				document.querySelector("#result").innerHTML = "<h1> Blue player Wins ! </h1>";
				$("#result").css({"color":"#2C93E8",
								  "text-align":"center"});
			}
			else if(status==10){
				document.querySelector("#result").innerHTML = "<h1> Red player Wins !!! </h1>";
				$("#result").css({"color":"red",
								  "text-align":"center"});
			}
			else if(turnNb>=8){
				document.querySelector("#result").innerHTML = "<h1> fin de partie : égalité</h1>";
				$("#result").css({"color":"grey",
								  "text-align":"center"});
			}
		}
		return gridData;
	}
}
