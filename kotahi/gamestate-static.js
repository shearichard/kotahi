var TCG = TCG || function () { };
TCG.MON = function () {
    _countStates = function () {
      var cnt = 0;
      $.each(TCG.MON.boardstates, function (idxboardstate, valboardstate) {
        cnt++;
      });
      return cnt;
    }
    _buildData = function () {
        //Extract the data which was written into gamestate.js
        return TCG.MDA.buildDataStructure();
    }
    _buildBoard = function () {
        XSTEP = 85;
        YSTEP = 85;
        XWIDTH = 80;
        YWIDTH = 80;
        ROWCOUNT = 10;
        COLCOUNT = 10;
        SQUAREFILLCOLOUR = 'lightslategray';
        CANVASFILLCOLOUR = 'whitesmoke';
        // create a wrapper around native canvas element (with id="c")
        var canvas = new fabric.Canvas('boardfacsimile',{backgroundColor : CANVASFILLCOLOUR});
        // create a rectangle object
        arrRect = [];
        for (var j = 0; j < ROWCOUNT; j++) {
            for (var i = 0; i < COLCOUNT; i++) {
                if ((j == 0) | (i == 0) | (j == (ROWCOUNT - 1)) | (i == (COLCOUNT - 1)))
                {
                    var rect = new fabric.Rect({
                        left: XSTEP * (i + 1) ,
                        top: YSTEP * (j + 1),
                        fill: SQUAREFILLCOLOUR,
                        width: XWIDTH,
                        height: YWIDTH
                    });
                    canvas.add(rect);
                }
            }
        }
    }
    _buildPropertyHoldingsChart = function () {
      var chartData = TCG.MON.buildPlayerPropertyHoldingsChartData();
      TCG.MON.playerPropHldngChart = c3.generate({
          title: {
            text: 'Property Holdings'
          },
          data: {
              columns: chartData 
          },
          axis: {
            y: {
              max: 5000,
              min: 0,
              label: {
                text: 'Value of Property',
                position: 'outer-middle'
              }
            },
            x: {
              label: {
                text: 'Turns',
                position: 'outer-center'
              }
            },
          },
          bindto: '#chartplayerproperty'
        });
        TCG.MON.playerPropHldngChart.data.columns = chartData; 
    }
    _buildFundsChart = function () {
      var chartData = TCG.MON.buildPlayerFundsChartData();
      TCG.MON.playerFundsChart = c3.generate({
          title: {
            text: 'Player Funds'
          },
          data: {
              columns: chartData 
          },
          axis: {
            y: {
              max: 5000,
              min: 0,
              label: {
                text: 'Cash on Hand',
                position: 'outer-middle'
              }
            },
            x: {
              label: {
                text: 'Turns',
                position: 'outer-center'
              }
            },
          },
          bindto: '#chartplayerfunds'
        });
        TCG.MON.playerFundsChart.data.columns = chartData; 
    }
    return {
      //PUBLIC AREA
      boardstates : null,
      boardstateslength : null,
      boardidx : 0,
      intHandle : null, 
      playerFundsChart : null,
      playerPropHldngChart : null,

      buildPlayerPropertyHoldingsChartData : function () {
        var outval = [];
        var innerval = null; 
        var currentPlayer = null;
        var FIRSTSTATE = 0;
        var arrPlayerPropHistory = [];
        var objPlayerPropHistory = {};
        var arrPlayers = [];
        //Iterate over first state to get the players involved
        $.each(TCG.MON.boardstates[FIRSTSTATE].playerstate, function (idxfirstateplyr, valfirststateplyr) {
          arrPlayers.push(valfirststateplyr.player);
          objPlayerPropHistory[valfirststateplyr.player] = [];
        });
        //Iterate over each of the players
        $.each(arrPlayers, function (idxplayer, valplayer) {
          //Iterate over each of the boardstates
          $.each(TCG.MON.boardstates, function (idxboardstate, valboardstate) {
            if (idxboardstate <= TCG.MON.boardidx)
            {
              //Accumulate property value owned by current 
              //player in current board state
              //TODO Need to initialize within the array rather tahn directly to objPlayer[valplayer]
              //TODO Also need to accumulate values within the array rather than overwriting on every
              //TODO loop
              //objPlayers[valplayer] = ;
              var propvaltot = 0;
              $.each(valboardstate.boardstate, function (idxsquare, valsquare) {
                if (valsquare.ownedby == valplayer){
                  propvaltot += parseInt(valsquare.price);
                }
              });
              objPlayerPropHistory[valplayer].push(propvaltot)
            }else{
              objPlayerPropHistory[valplayer].push(0)
            }
          });
        });
        $.each(arrPlayers, function (idxplayer, valplayer) {
          var arrwork = [valplayer];
          $.merge( arrwork, objPlayerPropHistory[valplayer] )
          arrPlayerPropHistory.push(arrwork);
        });
        return arrPlayerPropHistory
      },
      buildPlayerFundsChartData : function () {
        //We're looking to build something that looks like this . 
        //
        //var outval = [
        //    ['player1', 150, 200, 250, 400, 150, 250, null, null, null ],
        //    ['player2', 150, 200, 250, 40, 15, 25, null, null, null ]
        //]
        //
        //Here we have only two players but in reality we would have as many 
        //players as there was in the input data. Each player would have as many 
        //values as there are turns. 
        //
        //For the first turn all but one values would be null and only
        //the first value would a 'real' value. For the second turn the first two values
        //would be a 'real' value and all the others null and so on. In this way we
        //will have a fixed width graph on which the recorded values 'grow'
        var outval = [];
        var innerval = null; 
        var currentPlayer = null;
        var FIRSTSTATE = 0;
        //Iterate over first state to get the players involved
        $.each(TCG.MON.boardstates[FIRSTSTATE].playerstate, function (idxfirstateplyr, valfirststateplyr) {
          currentPlayer = valfirststateplyr.player;
          innerval = [];
          innerval.push(currentPlayer);
          //Iterate over each of the board states
          $.each(TCG.MON.boardstates, function (idxboardstate, valboardstate) {
            //Iterate over each of the players within this state looking
            //for the current player
            $.each(valboardstate.playerstate, function (idxstateplayer, valstateplayer) {
              if (valstateplayer.player == currentPlayer){
                if (idxboardstate <= TCG.MON.boardidx)
                {
                  innerval.push(valstateplayer.funds);
                }
                else
                {
                  innerval.push(0);
                }
              }
            });
          });
          outval.push(innerval);
        });
        return outval
      },
      buildChartDatav0 : function () {
                var outval = [
                    ['player1', 150, 200, 250, 400, 150, 250,null ,null ,null ],
                    ['player2', 150, 200, 250, 40, 15, 25, null, null,null ]
                ]
                return outval
      },
      pageElementsInitialization : function () {
        TCG.MON.boardstates = _buildData();
        TCG.MON.boardstateslength = _countStates();
        _buildFundsChart();
        _buildPropertyHoldingsChart();
        _buildBoard();
        TCG.MON.counterInitialization();
    },
    reflectPerTurnChangeOfStatus: function () {
      return function(){
        if (TCG.MON.boardidx >= TCG.MON.boardstateslength)
        {
          clearInterval(TCG.MON.intHandle)
        }
        else
        {
          $("#countervalue").html(TCG.MON.boardidx);
          _buildFundsChart();
          _buildPropertyHoldingsChart();
          TCG.MON.boardidx += 1;
        }
      };
    },
    counterInitialization: function () {
      TCG.MON.boardidx = 0;
      TCG.MON.intHandle = setInterval(TCG.MON.reflectPerTurnChangeOfStatus(), 200);
    }    
  };
}();
$(document).ready(function () { 
    TCG.MON.pageElementsInitialization();
});
