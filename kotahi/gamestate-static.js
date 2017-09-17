var TCG = TCG || function () { };
TCG.MON = function () {
    foo = function () {
      //
    }
    bar = function() {
      //
    }
    _buildData = function () {
        //Extract the data which was written into gamestate.js
        console.log("buildData");
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
      boardidx : 0,
      intHandle : null, 
      playerFundsChart : null,

      buildChartData : function () {
                var outval = [
                    ['player1', 150, 200, 250, 400, 150, 250,null ,null ,null ],
                    ['player2', 150, 200, 250, 40, 15, 25, null, null,null ]
                ]
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
        if (TCG.MON.boardidx >= 12)
        {
         clearInterval(TCG.MON.intHandle)
        }
        $("#countervalue").html(TCG.MON.boardidx);
        TCG.MON.boardidx += 1;
        console.log(TCG.MON.boardstates[TCG.MON.boardidx].boardstate[1].ownedby);
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
