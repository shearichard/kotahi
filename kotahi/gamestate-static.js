var TCG = TCG || function () { };
TCG.MON = function () {
    foo = function () {
      //
    }
    bar = function() {
      //
    }
    return {
        //PUBLIC AREA
        pageElementsInitialization : function () {
          alert("Module active");
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
        },
    };
}();
$(document).ready(function () { 
    TCG.MON.pageElementsInitialization();
});
