from time import sleep
import numpy as np
from numpy.linalg import norm
from pinocchio import SE3, AngleAxis, Quaternion

def _lerp(p0, p1, t):
    return (1 - t) * p0 + t * p1

def slerp(q0, q1, t):
    assert (t >= 0 and t <= 1)
    return q0.slerp(t,q1)

def nlerp(q0, q1, t):
    q0 = q0.coeffs()
    q1 = q1.coeffs()
    lerp = _lerp(q0, q1, t)
    lerp /= norm(lerp)
    return Quaternion(lerp[3], *list(lerp[:3]))

#adding second box to compare interpolations
viz.addBox('world/boxslerp', [.1, .2, .3], [1, 0, 0, 1])

q0 = Quaternion(SE3.Random().rotation)
q1 = Quaternion(SE3.Random().rotation)
viz.applyConfiguration('world/boxslerp', [0 ,.5, 0] + list(q0.coeffs()))
viz.applyConfiguration('world/box'     , [0 , 0, 0] + list(q0.coeffs()))
sleep(.1)
for t in np.arange(0, 1, .01):
    qn = nlerp(q0, q1, t)
    qs = slerp(q0, q1, t)
    viz.applyConfiguration('world/boxslerp', [0 ,.5, 0] + list(qs.coeffs()))
    viz.applyConfiguration('world/box'     , [0 , 0, 0] + list(qn.coeffs()))
    sleep(.01)
sleep(.1)
viz.applyConfiguration('world/box'     , [0,  0, 0] + list(q1.coeffs()))
viz.applyConfiguration('world/boxslerp', [0, .5, 0] + list(q1.coeffs()))

