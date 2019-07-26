function makeTeamList(teamData, namesData, teamsData) {
    // Take it step by step.

	var teama = teamData.team;
	var teamId = teama.id;
	var teamCoachName = teama.coach
	
	
	for (var i in teamsData){
		
		if(teamsData[i].id === teamId){
			var teamloc = teamsData[i].team;
			
		}
	}
	var firstele = teamloc + ', ' + "coached by "+  teamCoachName;
	
	var temparr={};
	var teamplayer = teamData.players;
	
	for (var i in namesData){
		for (var j in teamplayer){
			if(namesData[i].id === teamplayer[j].id){
				temparr[namesData[i].name] = teamplayer[j].matches;
				break;				
			}
			
		}
		
	}
	
	var newdict = Object.keys(temparr).sort(function(a,b){return temparr[b]-temparr[a]});
	var res  =[];
	var count = 1;
	for(var i in newdict){
		var newstr = count + ". " + newdict[i];
		res[count] = newstr;
		count ++;
	}
	res[0] = firstele;

    return res;
}

const teamJson = process.argv[2];
const namesJson = process.argv[3];
const teamsJson = process.argv[4];
if (teamJson === undefined || namesJson === undefined || teamsJson === undefined) {
  throw new Error(`input not supplied`);
}

// some sample data
const team  = require(`./${teamJson}`);
const names  = require(`./${namesJson}`);
const teams  = require(`./${teamsJson}`);
console.log(makeTeamList(team, names.names, teams.teams));
