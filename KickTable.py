from Point import *

JLSTZ01 = [Point( 0, 0), Point(-1, 0), Point(-1, 1), Point( 0,-2), Point(-1,-2)]
JLSTZ10 = [Point( 0, 0), Point( 1, 0), Point( 1,-1), Point( 0, 2), Point( 1, 2)]

JLSTZ12 = [Point( 0, 0), Point( 1, 0), Point( 1,-1), Point( 0, 2), Point( 1, 2)]
JLSTZ21 = [Point( 0, 0), Point(-1, 0), Point(-1, 1), Point( 0,-2), Point(-1,-2)]

JLSTZ23 = [Point( 0, 0), Point( 1, 0), Point( 1, 1), Point( 0,-2), Point( 1,-2)]
JLSTZ32 = [Point( 0, 0), Point(-1, 0), Point(-1,-1), Point( 0, 2), Point(-1, 2)]

JLSTZ30 = [Point( 0, 0), Point(-1, 0), Point(-1,-1), Point( 0, 2), Point(-1, 2)]
JLSTZ03 = [Point( 0, 0), Point( 1, 0), Point( 1, 1), Point( 0,-2), Point( 1,-2)]

JLSTZ_KICK_CLOCKWISE = [JLSTZ01, JLSTZ12, JLSTZ23, JLSTZ30]
JLSTZ_KICK_COUNTERCLOCKWISE = [JLSTZ03, JLSTZ10, JLSTZ21, JLSTZ32]

I01 = [Point( 0, 0), Point(-2, 0), Point( 1, 0), Point(-2,-1), Point( 1, 2)]
I10 = [Point( 0, 0), Point( 2, 0), Point(-1, 0), Point( 2, 1), Point(-1,-2)]

I12 = [Point( 0, 0), Point(-1, 0), Point( 2, 0), Point(-1, 2), Point( 2,-1)]
I21 = [Point( 0, 0), Point( 1, 0), Point(-2, 0), Point( 1,-2), Point(-2, 1)]

I23 = [Point( 0, 0), Point( 2, 0), Point(-1, 0), Point( 2, 1), Point(-1,-2)]
I32 = [Point( 0, 0), Point(-2, 0), Point( 1, 0), Point(-2,-1), Point( 1, 2)]

I30 = [Point( 0, 0), Point( 1, 0), Point(-2, 0), Point( 1,-2), Point(-2, 1)]
I03 = [Point( 0, 0), Point(-1, 0), Point( 2, 0), Point(-1, 2), Point( 2,-1)]

I_KICK_CLOCKWISE = [I01, I12, I23, I30]
I_KICK_COUNTERCLOCKWISE = [I03, I10, I21, I32]

O00 = [Point( 0, 0), Point( 0, 0), Point( 0, 0), Point( 0, 0), Point( 0, 0)]
O_KICK = [O00, O00, O00, O00]

KICK_CLOCKWISE = [
    I_KICK_CLOCKWISE,
    JLSTZ_KICK_CLOCKWISE,
    JLSTZ_KICK_CLOCKWISE,
    O_KICK,
    JLSTZ_KICK_CLOCKWISE,
    JLSTZ_KICK_CLOCKWISE,
    JLSTZ_KICK_CLOCKWISE
]

KICK_COUNTERCLOCKWISE = [
    I_KICK_COUNTERCLOCKWISE,
    JLSTZ_KICK_COUNTERCLOCKWISE,
    JLSTZ_KICK_COUNTERCLOCKWISE,
    O_KICK,
    JLSTZ_KICK_COUNTERCLOCKWISE,
    JLSTZ_KICK_COUNTERCLOCKWISE,
    JLSTZ_KICK_COUNTERCLOCKWISE
]