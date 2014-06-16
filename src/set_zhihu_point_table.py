import cPickle

point_table = {}
point_table[( 4, 4)] = 400.
point_table[( 3, 4)] = 270.
point_table[( 2, 4)] = 170.
point_table[( 1, 4)] = 100.
point_table[( 0, 4)] = 0.
point_table[(-1, 4)] = 0.
point_table[(-2, 4)] = 0.
point_table[(-3, 4)] = 0.
point_table[(-4, 4)] = 0.

point_table[( 4, 3)] = 240.
point_table[( 3, 3)] = 300.
point_table[( 2, 3)] = 200.
point_table[( 1, 3)] = 120.
point_table[( 0, 3)] = 0.
point_table[(-1, 3)] = 0.
point_table[(-2, 3)] = 0.
point_table[(-3, 3)] = 0.
point_table[(-4, 3)] = 0.

point_table[( 4, 2)] = 140.
point_table[( 3, 2)] = 180.
point_table[( 2, 2)] = 240.
point_table[( 1, 2)] = 160.
point_table[( 0, 2)] = 10.
point_table[(-1, 2)] = 0.
point_table[(-2, 2)] = 0.
point_table[(-3, 2)] = 0.
point_table[(-4, 2)] = 0.

point_table[( 4, 1)] = 100.
point_table[( 3, 1)] = 110.
point_table[( 2, 1)] = 150.
point_table[( 1, 1)] = 200.
point_table[( 0, 1)] = 40.
point_table[(-1, 1)] = 0.
point_table[(-2, 1)] = 0.
point_table[(-3, 1)] = 0.
point_table[(-4, 1)] = 0.

point_table[( 4, 0)] = 0.
point_table[( 3, 0)] = 0.
point_table[( 2, 0)] = 10.
point_table[( 1, 0)] = 20.
point_table[( 0, 0)] = 160.
point_table[(-1, 0)] = 20.
point_table[(-2, 0)] = 10.
point_table[(-3, 0)] = 0.
point_table[(-4, 0)] = 0.

point_table[( 4,-1)] = 0.
point_table[( 3,-1)] = 0.
point_table[( 2,-1)] = 0.
point_table[( 1,-1)] = 0.
point_table[( 0,-1)] = 40.
point_table[(-1,-1)] = 200.
point_table[(-2,-1)] = 150.
point_table[(-3,-1)] = 110.
point_table[(-4,-1)] = 100.

point_table[( 4,-2)] = 0.
point_table[( 3,-2)] = 0.
point_table[( 2,-2)] = 0.
point_table[( 1,-2)] = 0.
point_table[( 0,-2)] = 10.
point_table[(-1,-2)] = 160.
point_table[(-2,-2)] = 240.
point_table[(-3,-2)] = 180.
point_table[(-4,-2)] = 140.

point_table[( 4,-3)] = 0.
point_table[( 3,-3)] = 0.
point_table[( 2,-3)] = 0.
point_table[( 1,-3)] = 0.
point_table[( 0,-3)] = 0.
point_table[(-1,-3)] = 120.
point_table[(-2,-3)] = 200.
point_table[(-3,-3)] = 300.
point_table[(-4,-3)] = 240.

point_table[( 4,-4)] = 0.
point_table[( 3,-4)] = 0.
point_table[( 2,-4)] = 0.
point_table[( 1,-4)] = 0.
point_table[( 0,-4)] = 0.
point_table[(-1,-4)] = 100.
point_table[(-2,-4)] = 170.
point_table[(-3,-4)] = 270.
point_table[(-4,-4)] = 400.

cPickle.dump(point_table, open('../data/point_table.cpickle', 'wb'))
