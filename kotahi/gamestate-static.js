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
    return {
      //PUBLIC AREA
      boardstates : null,
      boardidx : 0,
      intHandle : null, 
      pageElementsInitialization : function () {
        //
        var chart = c3.generate({
            data: {
                columns: [
                    ['player1', 350, 200, 100, 400, 150, 250,null ,null ,null ],
                    ['player2', 350, 20, 10, 40, 15, 25, null, null,null ]
                ]
            },
            size: {
                width: 600 
            },
        });
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
        TCG.MON.boardstates = _buildData();
        TCG.MON.counterInitialization();
    },
    reflectPerTurnChangeOfStatus: function () {
      return function(){
        if (TCG.MON.boardidx >= 22)
        {
         clearInterval(TCG.MON.intHandle)
        }
        $("#countervalue").html(TCG.MON.boardidx);
        TCG.MON.boardidx += 1;
        console.log(TCG.MON.boardidx);
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
