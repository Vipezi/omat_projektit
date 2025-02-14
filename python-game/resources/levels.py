m_level1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,2,2,2,3,3,3,2,9,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,8,9,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,7,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,7,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,7,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,8,2,2,2,2,3,3,3,2,2,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

m_house1 =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
           [0, 5, 5, 5, 5,5,5,5,5,5,5,5,5,5,5,0],
           [0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,0],
					 [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0],
					 [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0],
					 [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0],
					 [0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

levels = {
  "level1":{
		"map":m_level1,
		"x0":456,
		"y0":240,
		"elements":[
			{"name":"house","x":13*32,"y":5*32,"obstacle":True,"category":"buildings","transparent":True}
		]
  },
	"house1":{
		"map":m_house1,
		"elements":[
			{"name":"carpet","x":88,"y":228,"category":"decoration"}
		]
	}
}

transitions = {
  "level1":[
    {"y0":215,
     "y1":217,
		 "x0":380,
		 "x1":392,
     "new_x":88,
     "new_y":212,
     "level":"house1"
    }
  ],
	"house1":[
    {"x0":80,
		 "x1":100,
     "y0":218,
		 "y1":221,
     "new_x":387,
     "new_y":220,
     "level":"level1"
    }
  ]
}