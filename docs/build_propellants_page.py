import os
from rocketcea.input_cards import oxCards, fuelCards, propCards

oxL = sorted( oxCards.keys(), key=str.lower )
fuelL = sorted( fuelCards.keys(), key=str.lower )
propL = sorted( propCards.keys(), key=str.lower )


here = os.path.abspath(os.path.dirname(__file__)) # Needed to find fulltoc

fRST_name = os.path.join( here, 'propellants.rst' )
fRST_out = open(fRST_name, 'w')
fRST_out.write(""".. propellants


.. _`propellants_link`:

.. This file is generated by "build_propellants_page.py"

Propellants
===========

The table below displays the propellants built in to RocketCEA.
Click any of the names to see the card deck submitted to CEA for that propellant.

If your propellant is not included, or if you disagree with the definitions,
new propellants can be added, and existing propellants can be modified.

Any use of RocketCEA begins with an import statement and an instance of CEA_Obj::

    from rocketcea.cea_obj import CEA_Obj
    C = CEA_Obj( oxName='N2O4', fuelName='MMH')

Bipropellant runs use **oxName** and **fuelName** to define propellants.
For Monopropellants and Solid Propellants, the instance of CEA_Obj uses **propName**::

    from rocketcea.cea_obj import CEA_Obj
    C = CEA_Obj( propName='HYD40')

`Click Propellant Name to View Definition`

.. raw:: html

    <table width="100%">

""")
# add raw html table

def get_name( i, L ):
    try:
        name = L[i]
    except:
        name = ''
    return name


def make_html_row( i, L, nr=4 ):
    """make an html row of length=nt"""
    sL = ['    <tr>']
    for n in range(nr):
        j = i + n
        if j<len(L):
            sL.append( '<td><a href="#%s">%s</a></td>'%(L[j], L[j]) )
        else:
            sL.append( '<td> &nbsp; </td>' )
    sL.append( '</tr>\n' )
    return ''.join(sL)
    
nr=8
# Oxidizers
fRST_out.write('    <tr><td><table width="100%%"><tr><th colspan="%i" style="text-align:center;">Oxidizers</th></tr>\n'%nr)
for i in range(0, len(oxL), nr):
    fRST_out.write( make_html_row(i, oxL, nr ) )
fRST_out.write('    </table></td></tr>\n\n')

fRST_out.write('    <tr><td><table width="100%%"><tr><th colspan="%i" style="text-align:center;">Fuels</th></tr>\n'%nr)
for i in range(0, len(fuelL), nr):
    fRST_out.write( make_html_row(i, fuelL, nr ) )
fRST_out.write('    </table></td></td></tr>\n\n')

fRST_out.write('    <tr><td><table width="100%%"><tr><th colspan="%i" style="text-align:center;">Monoprop &amp; Solid</th></tr>\n'%nr)
for i in range(0, len(propL), nr):
    fRST_out.write( make_html_row(i, propL, nr ) )
fRST_out.write('    </table></td></td></tr>\n\n')

fRST_out.write('    </table>\n\n' )
# =======================================================

fRST_out.write("""

Special Blends
--------------

There are a number of special blends that can be created when making an instance of CEA_Obj.

Hydrazine Monopropellant
************************

The performance of :ref:`Hydrazine Monopropellant <hydrazine_mono_link>` engines is driven by the amount of ammonia dissociation that
the catalyst bed delivers. Any amount of ammonia dissociation can be run by calling out the **propName**
as "HYD" + weight percent dissociation. 

Note that the CEA FORTRAN code has been modified to include "Undissociated Ammonia (UA)" as an exhaust product.
The CEA input also includes an "omit NH3" statement to prevent normal NH3 calculations.

The examples below call out 30, 40 and 50 percent ammonia dissociation.::

    C = CEA_Obj( propName='HYD30')
    C = CEA_Obj( propName='HYD40')
    C = CEA_Obj( propName='HYD50')


MMH + N2H4
**********

Mixtures of MMH and N2H4 are often used to suppress the freezing point of N2H4.
M20 is a common mixture (20% MMH + 80% N2H4 by weight). The examples below call out 10, 20 and 30 percent MMH::

    C = CEA_Obj( oxName='N2O4', fuelName='M10')
    C = CEA_Obj( oxName='N2O4', fuelName='M20')
    C = CEA_Obj( oxName='N2O4', fuelName='M30')


Mixed Oxides of Nitrogen
************************

Mixtures of N2O4 and NO are often used to suppress the freezing point of N2O4.
MON25 is a common mixture (25% NO + 75% N2O4 by weight).

When NO is added to N2O4, there are two main equilibrium reactions::

    N2O4     <==> 2 NO2
    NO + NO2 <==> N2O3

For this reason, the input cards for MON oxidizers include N2O4 and N2O3.
The weight percentages are calculated based on the equilibrium equations above.

The examples below call out MON oxidizers with 15, 20 and 25 percent NO::

    C = CEA_Obj( oxName='MON15', fuelName='MMH')
    C = CEA_Obj( oxName='MON20', fuelName='MMH')
    C = CEA_Obj( oxName='MON25', fuelName='MMH')


Peroxide + Water
****************

Peroxide is often blended with water in order to enhance its stability and improve its safety.
While the debate about an appropriate blend of Peroxide rages on, analyzing it with RocketCEA
simply requires calling it out as "Peroxide" + weight percent Peroxide.
The examples below call out 90, 95 and 98 percent Peroxide::

    C = CEA_Obj( propName='Peroxide90')
    C = CEA_Obj( propName='Peroxide95')
    C = CEA_Obj( propName='Peroxide98')
    C = CEA_Obj(   oxName='Peroxide98', fuelName="MMH")


FLOX
****

FLOX is a mixuture of Fluorine and Oxygen.
Call out the mixture as "FLOX" + weight percent of Fluorine.
The examples below call out 60, 70 and 80 percent Fluorine::

    C = CEA_Obj(   oxName='FLOX60', fuelName="LH2")
    C = CEA_Obj(   oxName='FLOX70', fuelName="LH2")
    C = CEA_Obj(   oxName='FLOX80', fuelName="LH2")

""")

# =======================================================
fRST_out.write('\n\nOxidizers\n---------\n\n' )

for name in oxL:
    fRST_out.write('.. raw:: html\n\n')
    fRST_out.write('    <a name="%s"></a> \n\n'%name )

    fRST_out.write('%s\n%s\n\n'%(name, '*'*len(name)) )
    
    fRST_out.write('::\n\n')
    cardL = oxCards[name]
    for card in cardL:
        fRST_out.write('    ' + card.strip() + '\n' )
    fRST_out.write('\n\n')
        
# =======================================================
fRST_out.write('\n\nFuels\n-----\n\n' )

for name in fuelL:
    fRST_out.write('.. raw:: html\n\n')
    fRST_out.write('    <a name="%s"></a> \n\n'%name )

    fRST_out.write('%s\n%s\n\n'%(name, '*'*len(name)) )
    
    fRST_out.write('::\n\n')
    cardL = fuelCards[name]
    for card in cardL:
        fRST_out.write('    ' + card.strip() + '\n' )
    fRST_out.write('\n\n')
        
# =======================================================
fRST_out.write('\n\nMonoprop & Solid\n----------------\n\n' )

for name in propL:
    fRST_out.write('.. raw:: html\n\n')
    fRST_out.write('    <a name="%s"></a> \n\n'%name )

    fRST_out.write('%s\n%s\n\n'%(name, '*'*len(name)) )
    
    fRST_out.write('::\n\n')
    cardL = propCards[name]
    for card in cardL:
        fRST_out.write('    ' + card.strip() + '\n' )
    fRST_out.write('\n\n')
        
    
    

fRST_out.close()