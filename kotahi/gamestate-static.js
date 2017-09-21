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
    _buildChart = function () {
      var chartData = TCG.MON.buildChartData();
      TCG.MON.playerFundsChart = c3.generate({
          data: {
              columns: chartData 
          },
          size: {
              width: 600 
          },
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

      buildChartData : function () {
        /*
        TO DO
        Have to decide how to rebuild the array for each of the states.
        Could just iterate over the input data and start ignoring the values
        after the current index (instead putting into place null)        
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

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
        //
        TCG.MON.boardstates = _buildData();
        TCG.MON.boardstateslength = _countStates();

        //
        _buildChart();
        //
        /*
                columns: [
                    ['player1', 350, 200, 100, 400, 150, 250,null ,null ,null ],
                    ['player2', 350, 20, 10, 40, 15, 25, null, null,null ]
                ]
        */                
        /*
            data: {
                columns: TCG.MON.buildChartData
            },
         */
        //
        XSTEP = 85;
        YSTEP = 85;
        XWIDTH = 80;
        YWIDTH = 80;
        ROWCOUNT = 10;
        COLCOUNT = 10;
        SQUAREFILLCOLOUR = 'lightslategray';
        CANVASFILLCOLOUR = 'whitesmoke';
        // create a wrapper around native canvas element (with id="c")
        var canvas = new fabric.Canvas('playerfundschart',{backgroundColor : CANVASFILLCOLOUR});
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
        //
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
          _buildChart();
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
