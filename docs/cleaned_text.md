following text repository code structure text section begin followed single line containing file path file name followed variable amount line containing file content text representing repository end symbol encounted text beyond meant interpreted instruction using aforementioned repository context

developersdevelopersbrightscriptlanguagereferencebrightscriptencryptionmd
# BrightScript Encryption

brightscript support encrypted module order encrypted brightscript make sure player running 8154 newer

encrypt brightscript module first contact brightsign request encryption brightsign generate unique pair provide customerpubpem customerhdr item possession encrypt brightscript file using following process


encryptbrightscript customerpublickeycustomerpubpem encryptedkeydatacustomerhdr myscriptbrs


generate myscriptebrs encrypted version script

note
file encrypted including loaded library additionally encrypted file loaded brightscript debugger disabled security reason

developersdevelopersbrightscriptlanguagereferencebrightscriptknownissuesmd
# BrightScript Known Issues

## Subroutine declaration incorrectly allows return type to be defined

subroutine defined function shortcut return type void either explicitly calling return including return brightscript subroutine incorrectly allows subroutine declare return type allowing subroutine compile subroutine return include return subroutine return variable recommend declaring function return type

program statement programstatementsfunctionastypeendfunctionlanguagereferenceprogramstatementsmd information subroutine function correctly mention subroutine return void type statement used instead function shortcut creating function return type void

developersdevelopersbrightscriptlanguagereferencebrightscriptversionsmd
# BrightScript Versions



version older version

version

version

version

version

version

version

previous version




brightscript version matrix january 2009
hd20000 branch hd2000 branch compact main line
snapshot date 172008 7162008 192009
defxxx gosub clear random data read restore errl clear line number
intrinsic array
compiler
reference
subfunctions
ifenum
fornext always execute least
exit
invalid type error used zero invalid added roinvalid invalid autoboxing
array roarray added ifarray
uninit usage longer allowed
like function
roxml element
type change match declaration name integer roint32
added roboolean
added dynamic type type optional subfunctions
andor dont eval unneeded term
subfun default parameter value integer
declaration
array declaration
change array
anonymous function
added circ garbage collector
eval

developersdevelopersbrightscriptlanguagereferencebuiltinfunctionsmd
# Built-In Functions



version older version

version

version

version

version

version

version

previous version




table content

typetype
getglobalaagetglobalaa
rndrnd
boxbox
runrun
evaleval
getlastruncompileerrorgetlastruncompileerror
getlastrunruntimeerrorgetlastrunruntimeerror

brightscript feature builtin modulescope intrinsic function number file string mathematics system function also available roglobal object

## Type()

typea variable string

function return type passed variable andor object

## GetGlobalAA()

getglobalaa object

function fetch global associative array current script

## Rnd()

rndrange integer integer
rnd0 float

passed positive nonzero integer function return pseudorandom integer argument value range includes argument value example calling rnd55 return pseudorandom integer greater less

argument function return pseudorandom float value

note
note
function utilize pseudorandom seed number generated internally accessible user

## Box()

boxtype dynamic object

function return object version specified intrinsic type object passed

##### **Example**


boxstring
boxb change


## Run()

runfilename string optionalarg dynamic dynamic
runfilenames roarray optionalarg dynamic dynamic

function run script current script append optional argument passed main function script called script also return argument caller script

string file name passed function compile corresponding file array file passed function compile file link together

##### **Example**


main
runtestbrs
breakifrunerrorlinenum
print runtest2brs
runfile1brsfile2brs4 stop
breakifrunerrorlinenum
stop



breakifrunerrorln
elgetlastruncompileerror
elinvalid
elgetlastrunruntimeerror
elhfc elhe2 return
fcerrnormalend e2errvaluereturn
print runtime error line
stop
else
print compile error line


print



stop




## Eval()

evalcodesnippet string dynamic

function run passed code snippet context current function function compiles snippet executes bytecode code compiles run successfully return zero code compiles successfully encounter runtime error return integer indicating error code using code getlastrunruntimeerror function compilation fails return rolist object rolist structure identical getlastruncompileerror function

eval function useful case

need dynamically generate code runtime

need execute statement could result runtime error dont want code execution stop


##### **Example**


print eval10 return divide zero error


## GetLastRunCompileError()

getlastruncompileerror rolist

function return rolist object containing compile error invalid error occurred rolist entry roassociativearray object containing following key

errstr compile error type string

filespec file script containing error string

errno error number integer

lineno line number error occurs integer


following possible errno value



error code description expanded description
errnw endwhile statement occurs without statement
errmissingendwhile statement occurs without endwhile statement
errmissingendif script reached without finding endif statement
errnoln line number found
errlnseq line number sequence error
errloadfile error loading file
errnomatch match statement match
errunexpectedeof unexpected string encountered string compilation
errfornextmismatch variable next match
errnoblockend
errlabeltwice label defined
erruntermedstring literal string quote
errfunnotexpected
errtoomanyconst
errtoomanyvar
errexitwhilenotinwhile
errinternallimitexceded
errsubdefinedtwice
errnomain
errforeachindextm
errretcannothavevalue
errretmusthavevalue
errfunmusthaverettype
errinvalidtype
errnolonger feature longer supported
errexitfornotinfor
errmissinginitilizer
erriftoolarge
errronotfound
errtoomanylabels
errvarcannotbesubname
errinvalidconstname
errconstfolding

## GetLastRunRuntimeError()

getlastrunruntimeerror integer

function return error code resulted last function

code indicate normal result



error code description expanded description
errokay
errnormalend execution ended normally termination shell exit window closed
errvaluereturn return executed value returned stack
errnovaluereturn return executed without value returned stack

following code indicate runtime error



error code description expanded description
errinternal unexpected condition occurred
errundefinedopcd opcode could handled
errundefinedop expression operator could handled
errmissingparn
errstackunder value stack
errbreak scriptbreak function called
errstop stop statement executed
errro0 bscnewcomponent failed object class found
errr01 brightscript member function call right number parameter
errro2 brightscript member function found object interface
errro3 brightscript interface member object
errtoomanyparam many function parameter handle
errwrongnumparam number function parameter incorrect
errrvig function return value ignored
errnotprintable value printable
errnotwaitable wait statement cannot applied object object romessageport interface
errmustbestatic interface call rotinterface type must static
errro4 operator used object contain legal object interface reference
errnotypeop operation attempted typeless operand
erruseofuninitvar uninitialized variable used illegally
errtm2 nonnumeric index applied array
errarraynotdimmed
erruseofuninitbrsubref reference uninitialized
errmusthavereturn
errinvalidlvalue left side expression invalid
errinvalidnumarrayidx number array index invalid
errunicodenotsupported
errnotfunopable
errstackoverflow
errcn continue cont allowed
errstringtolong
erros string space
errtm type mismatch string number operation mismatch occurred
errdivzero
errdd attempted redimension array
errbs array subscript bound
errmissingln
erroutofmem
errfc invalid parameter passed functionarray negative matrix square root
errod data read
errrg return without gosub
errsyntax
errnf next without

developersdevelopersbrightscriptlanguagereferencecorelibraryextensionmd
# Core Library Extension



version older version

version

version

version

version

version

version

previous version


number builtin function part brightscript core library librarylanguagereferenceprogramstatementsmd statement include subset function


library v30bslcorebrs


##### bslBrightScriptErrorCodes() As roAssociativeArray

return associative array namevalue pair corresponding brightscript error code description

##### bslGeneralConstraints() As roAssociativeArray

return associative array namevalue pair corresponding system constant

##### bslUniversalControlEventCodes() As roAssociativeArray

return associative array namevalue pair corresponding remote code constraint

##### AsciiToHex(ascii As String) As String

return hexformatted version passed ascii string

##### HexToAscii(hex As String) As String

return asciiformatted version passed string

##### HexToInteger(hex As String) As Integer

return integer value passed string

developersdevelopersbrightscriptlanguagereferenceeventsmd
# Events



version older version

version

version

version

version

version

version

previous version


event brightscript center around event loop romessageport object brightscript object post message port form event object example rotimer object post event type rotimerevent configured interval reached

following script set destination message port using setport method wait event form rogpiobutton object process event


print brightsign buttonled test running
createobjectromessageport
gpio createobjectrogpiocontrolport
gpiosetportp

true
msgwait0
typemsgrogpiobutton
butn msggetint
butn
gpiosetoutputstatebutn171
print button pressed butn
sleep500
gpiosetoutputstatebutn170



ignore button pressed flashing
pgetmessageinvalid




note line replaced using following substituting





developersdevelopersbrightscriptlanguagereferenceexamplescriptmd
# Example Script



version older version

version

version

version

version

version

version

previous version


following code us gpio button control work brightsign model video output gpio port



game snake
demonstrates brightscript programming concept
june 2008


every brightscript program must single main


main

gameboardnewgameboard

true
gameboardsetsnakenewsnakegameboardstartx gameboardstarty
gameboarddraw
gameboardeventloop
gameboardgameover exitwhile







game board object






example brightscript constructor newgameboard regular function module scope
brightscript object dynamic created runtime class
object container brightscript component type roassocitivearray
used hold member data member function


function newgameboard object
gameboardcreateobjectroassociativearray create brightscript component typeclass roassociativearray
gameboardinitgbinit entry type rofunction value gbdraw defined module
gameboarddrawgbdraw
gameboardsetsnakegbsetsnake
gameboardeventloopgbeventloop
gameboardgameovergbgameover
gameboardstartxgbstartx
gameboardstartygbstarty
gameboardinit call init member function gbinit

return gameboard

function



gbinit member function gameboard brightscript object
called pointer appropriate instance
brightscript bytecode interpreter

function gbinit void

button press message port

mbuttons createobjectromessageport
mgpio createobjectrogpiocontrolport
mgpiosetportmbuttons


determine optimal size position snake gameboard

cellwid16 cell game pixel width
cellhi16 cell height
maxwide30 width cell game board
maxhi30 height cell game board
vidmodecreateobjectrovideomode
wcintvidmodegetresxcellwid
wmaxwide maxwide
hcintvidmodegetresycellhi
hmaxhi hmaxhi

xpix cintvidmodegetresx wcellwid2 center game board screen
ypix cintvidmodegetresy hcellhi2 center game board screen


create text field square char cell size

metacreateobjectroassociativearray
metaaddreplacecharwidthcellwid
metaaddreplacecharheightcellhi
metaaddreplacebackgroundcolorh202020 dark grey
metaaddreplacetextcolorh00ff00 green
mtextfieldcreateobjectrotextfieldxpixypixwhmeta
typemtextfieldrotextfield
print unable create rotextfield
stop
endif
function


object refers type brightscript component
pointer

gbsetsnakesnake object
msnakesnake



function gbstartx integer
return cintmtextfieldgetwidth2
function


function gbstarty integer
return cintmtextfieldgetheight2
function


function gbeventloop void

tickcount0

true
msgwait250 mbuttons wait button 250ms second timeout
typemsgrogpiobutton
msggetint1 msnaketurnnorth
msggetint2 msnaketurnsouth
msggetint3 msnaketurneast
msggetint4 msnaketurnwest
else time happened move snake forward
tickcounttickcount1
tickcount6
tickcount0
msnakemakelongermtextfield return
else
msnakemoveforwardmtextfield return
endif
endif


function


gbdraw

given rotextfield object mtextfield draw around edge


solid191 graphic enabled
mtextfieldcls

mtextfieldgetwidth1
print mtextfieldwchrsolid
print mtextfieldmtextfieldgetwidthmtextfieldgetheight1wchrsolid


mtextfieldgetheight2
print mtextfieldhmtextfieldgetwidthchrsolid
print mtextfieldhmtextfieldgetwidthmtextfieldgetwidth1chrsolid


msnakedrawmtextfield



function gbgameover boolean

msg0
width mtextfieldgetwidth
height mtextfieldgetheight

true
print mtextfieldwidthheight21widthlenmsg2msg
sleep300
print mtextfieldwidthheight21widthlenmsg2msg0
sleep150
getmessage return message object message available
mbuttonsgetmessage invalid return false
endwhile

function





snake object





construct snake brightscript object

function newsnakex integer integer object

create brightscript component container brightscript object
snakecreateobjectroassociativearray
snakedrawsnkdraw
snaketurnnorthsnkturnnorth
snaketurnsouthsnkturnsouth
snaketurneastsnkturneast
snaketurnwestsnkturnwest
snakemoveforwardsnkmoveforward
snakemakelongersnkmakelonger
snakeaddsegmentsnkaddsegment
snakeeraseendbitsnkeraseendbit


snake list line segment
line segment roassociativearray conains length direction given delta needed move drawn


snakeseglist createobjectrolist
snakeaddsegment103


position head snake

snakesnakexx
snakesnakeyy
snakebody191 graphic enabled
snakedx1 default snake direction move offset
snakedy0 default snake direction move offset

return snake

function


snkdrawtextfield object
xmsnakex
ymsnakey
mseglist
xdeltasegxdelta
ydeltasegydelta
seglen
textfieldsetcursorposx
textfieldsendbytembody
xxxdelta
yyydelta





snkeraseendbittextfield object
xmsnakex
ymsnakey
mseglist
xxseglensegxdelta
yyseglensegydelta


textfieldsetcursorposx
textfieldsendbyte32 ascii space could




function snkmoveforwardtextfield objectas boolean
meraseendbittextfield
tailmseglistgettail

following show member function perform
function brightscript operator behind scene used
point longer method illustration

lentaillookuplen taillen taillen brightscript syntax case sensative
len1
len0
mseglistremovetail
else
tailaddreplacelenlen taillenlen
endif

return mmakelongertextfield

function

function snkmakelongertextfield object boolean
msnakexmsnakexmdx
msnakeymsnakeymdy
textfieldsetcursorposmsnakex msnakey
textfieldgetvaluembody return true
textfieldsendbytembody
head mseglistgethead
headlenheadlen1
return false
function

snkaddsegmentdx integer integer integer

aacreateobjectroassociativearray
aaaddreplacexdeltadx line segment draw head tail
aaaddreplaceydeltady
aaaddreplacelenlen
mseglistaddheadaa




snkturnnorth
mdx0 mdy1 mdx0mdy1maddsegmentmdx north


snkturnsouth
mdx0 mdy1 mdx0mdy1maddsegmentmdx south


snkturneast
mdx1 mdy0 mdx1mdy0maddsegmentmdx east


snkturnwest
mdx1 mdy0 mdx1mdy0maddsegmentmdx west



developersdevelopersbrightscriptlanguagereferencegarbagecollectionmd
# Garbage Collection



version older version

version

version

version

version

version

version

previous version


brightscript automatically free string longer used free object reference count go zero carried time object string longer used background garbage collection task result predictable garbagecollection process unexpected stall execution

object enter state circular reference counting object reference never reach reference count zero need freed manually using rungarbagecollector method method useful destroying presentation data structure creating presentation

developersdevelopersbrightscriptlanguagereferenceintrinsicobjectsmd
# Intrinsic Objects



version older version

version

version

version

version

version

version

previous version


general manual us term object refer brightscript component component interface member function brightscript us directly exception core object roarray roassociativearray roint romessageport brightscript object platform specific

create intrinsic object brightscript object brightscript component currently create brightscript component brightscript create intrinsic object interface intrinsic object contain member function property object

brightscript object simply roassociativearray member function called associative array pointer accessible inside function code access object key constructor brightscript simply normal function global scope creates roassociativearray instance fill member function property

snake game appendix example creating intrinsic object

developersdevelopersbrightscriptlanguagereferenceobjectsandinterfacesmd
# Objects and Interfaces



version older version

version

version

version

version

version

version

previous version




table content

brightscript objectsbrightscriptobjects
wrapper objectswrapperobjects
interfacesinterfaces
statement interface integrationstatementandinterfaceintegration
printprint
waitwait
expression parsingexpressionparsing
array operatorarrayoperator
member access operatormemberaccessoperator

## BrightScript Objects

though brightscript operates independently object architecture library required programming brightscript application brightsign platform exposed brightscript library object platform must register brightscript object expose part

brightscript object written compatible language robust version change script generally backwards compatible object undergone revision

brightscript object keep reference count delete reference count reach zero

## Wrapper Objects

intrinsic brightscript type boolean integer float double string invalid object equivalent intrinsic type passed function expects object appropriate wrapper object created assigned correct value passed function sometimes referred autoboxing allows example roarray object store value integer string well object

expression expects type work corresponding wrapper object well roboolean roint rofloat rodouble rostring

following example illustrate wrapper object work


print 5tostrth
print 5toint5

5tostr cause error instead following
5tostr

type5tostr string stop
5tostr5 stop
12tostr3 stop

itostr55 stop
100tostr100 stop
100tostr100 stop

ytostr10 stop

5toint5 type5tointinteger stop
5tofloat50 type5tofloatfloat stop
fs11
fstofloat11 fstoint1 stop

01234567left3012 stop
01234567right44567 stop
01234567mid334567 stop
01234567mid313 stop
01234567instr565 stop
01234567instr6561 stop
01234567instr000 stop


## Interfaces

interface brightscript operate similarly java microsoft interface known member function implement logic way interface similar virtual base class script program compatible object interface without regard type object belongs example roserialport object control standard serial interface implement three interface ifserialcontrol ifstreamreceive ifstreamsend since print statement sends output object ifstreamsend interface work roserialport object well object ifstreamsend interface

## Statement and Interface Integration

brightscript statement integrated functionality interface section describes statement interface

### PRINT

using print statement following format print object ifstreamsend interface including rotextfield roserialport object


port createobjectroserialport0115200
print port string


expression printed evaluates object ifenum interface print statement print every item enumerated

addition printing value intrinsic type print statement also used print object expose following interface ifstring ifint iffloat

### WAIT

wait statement work conjunction object ifmessageport interface

### Expression Parsing

expression expects certain type variableincluding integer float double boolean stringcan accept object interface equivalent type ifint iffloat ifdouble ifboolean ifstring

### Array Operator

array operator work object ifarray ifassociativearray interface including array associative array list

### Member Access Operator

member access operator operatorlanguagereferenceoperatorsmd work object ifassociativearray interface also work object used call member function method also special meaning used roxmlelement roxmllist object

developersdevelopersbrightscriptlanguagereferenceoperatorsmd
# Operators



version older version

version

version

version

version

version

version

previous version




table content

logical bitwise operatorslogicalandbitwiseoperators
operatordotoperator
associative arraysassociativearrays
array functioncall operatorsarrayandfunctioncalloperators
array dimensionsarraydimensions
equal operatorequalsoperator

operation innermost level parenthesis performed first evaluation proceeds according precedence following table operation precedence leftassociative except exponentiation rightassociative



description symbol
function call parenthesis
array operator
exponentiation
negation
multiplication division modulus
addition subtraction
comparison
logical negation
logical conjunction
logical

string operator following operator work string

function reference operator work variable contain function reference function literal

## Logical and Bitwise Operators

operator used logical boolean comparison argument operator boolean





notb print success


hand argument operator numeric perform bitwise operation


zero
true false false


operator used logical operation necessary amount expression executed example first statement print true second statement cause runtime error invalid valid operand


print true invalid
print false invalid


## Dot Operator

operator used brightscript object also special meaning used roassociativearray object well roxmlelement roxmllistxmlsupport object used brightscript object refers interface method associated object following example ifint refers interface setint refers method part interface


createobjectroint
iifintsetint5
isetint5


every object method part interface however specifying interface operator optional interface omitted third line example interface part object searched specified member naming conflict method name appears interface interface specified

### Associative Arrays

operator used associative array calling lookup addreplace method member function roassociativearraybrightscriptobjectreferencebrightscriptcoreobjectsroassociativearraymd object



aanewkey value
print aanewkey


note parameter operator compile time unlike lookup addreplace method dynamic

operator always case insensitive example statement aanewkey55 create entry newkey associative array generate casesensitive key instantiate roassociativearray object setmodecasesensitive method

## Array and Function-Call Operators

operator used access array brightscript object ifarray interface roarray rolist object also used access associative array operator take expression evaluated runtime operator take identifier compile time

operator used call function used function literal variable containing function reference function called

following code snippet demonstrates array functioncall operator


createobjectroassociativearray
aanewkey value
print aanewkey

array createobjectroarray true
array2
print array2

fivevar five
print fivevar

array1 fivevar
print array1 print

function five integer
return
function


### Array Dimensions

array brightscript dimensional multidimensional array implemented array array operator automatically multidimensionality example following fetching expression


array555
item array123
item array123


note
multidimensional array grows beyond hint size entry automatically roarray

## Equals Operator

operator used assignment comparison



print


unlike language brightscript support assignment operator inside expression meant eliminate common class bug caused confusion assignment comparison

assignment occurs intrinsic type copied brightscript object reference counted

developersdevelopersbrightscriptlanguagereferenceprogramstatementsmd
# Program Statements



version older version

version

version

version

version

version

version

previous version




table content

statement syntaxstatementsyntax
librarylibrary
dimdim
assignment assignment
endend
stopstop
gotogoto
returnreturn
printprint
forforendfor
forforeachinendfor
nesting statementsnestingforeachstatements
exit whilewhileexitwhile
elseifthenelse
block elseif endifblockifelseifthenendif
function type functionfunctionastypeendfunction

brightscript support following statement type note brightscript case sensitive syntax statement documented detail later chapter

library



assignment



stop

goto



print

step exit next

exit next

exit

function function return


##### **Example**


function main void

cavemen10

cavemenpushfred
cavemenpushbarney
cavemenpushwilma
cavemenpushbetty

caveman caveman
print caveman


function


## Statement Syntax

line contain single statement however colon used separate multiple statement single line

##### **Example**


myname fred
mynamefred yourname barneyprint yourname


## LIBRARY 

library filenamebrs

library statement allows include brightscript library file utilized script library statement must occur beginning script statement function operator

system locates library searching directory containing current script well sysscriptlib directory note function currently change path library statement called script system continue searching directory caller script hand running script directly brightsign shell modify library search path called script

first statement include library folder script second include library subfolder


library mybsl1brs
library newlibmybsl2brs


following statement include bslcorebrslanguagereferencecorelibraryextensionmd library useful brightscript feature sysscriptlib directory


library v30bslcorebrs


## DIM 

name dim1 dim2 dimk

dimension statement provides shortcut creating roarray object set variable name type roarray create array array needed multidimensionality dimension passed index maximum entry allocated array initial size dimension1 though array resized larger automatically needed

following line create identical array


array5
array createobjectroarray true


note
note
expression equivalent

following script demonstrates useful operation array



















printerror stop






## Assignment ("=")

variable expression

assignment statement assigns variable value

following line variable left side equal operator assigned value constant expression right side equal operator


rose rose
b1123
x223
xxb1


## END

statement terminates script execution normally

## STOP

stop statement interrupt script execution return stop error invokes debugger cont command debugger prompt continue execution script step command execute single step script

## GOTO

goto label

goto statement transfer program control line number specified label goto label statement result branching operation label identifier terminated colon line contains statement expression

##### **Example**


mylabel
print hello world
goto mylabel


## RETURN

return expression

return statement return function back caller function type void return also return value caller

## PRINT

print outputobject location item list

print statement print item list item console item string integer float variable expression object ifint iffloat ifstring interface also printed outputobject specified statement print object ifstreamsend interface

statement printing list item item must separated semicolon comma semicolon used space inserted printed item comma used cursor automatically advance next print zone printing next item

positive number zero printed leading space without plus sign space inserted string

##### **Example**


print equal
print equal


##### **Example**


string
print
print stringstring string string


print zone following example character wide cursor move next print zone time comma encountered


print zone 1zone 2zone 3zone
print zone zone zone zone


##### **Example**


print print statement
print print statement
print print statement print statement


case semicolon dropped example following statement legal


print five


trailing semicolon override cursorreturn next print statement begin last left trailing punctuation used print statement cursor drop beginning next line

#### \[@location\]

console printing iftextfield interface character specify printing begin

##### **Example**


print mtextfieldwidthheight21widthlenmsg2msg


whenever print bottom line display automatic linefeed cause displayed line move line prevent happening trailing semicolon statement

#### TAB (expression)

statement move cursor specified position current line modulo width console position greater console width

##### **Example**


print tab5tabbed 5tab25tabbed


note following statement

statement used several time print list

punctuation required statement

numerical expression used specify position

statement cannot used move cursor left

cursor beyond specified position statement ignored


#### POS(x)

statement return integer indicates current cursor position maximum width window statement requires dummy argument form numeric expression


print tab40 pos0 print position

print tabpos05words tabpos05are
print tabpos05evenly tabpos05spaced


## FOR / END FOR

countervariable initialvalue finalvalue step increment next

statement creates iterative loop allows sequence program statement executed specified number time

initialvalue finalvalue increment expression first time statement executed three variable evaluated value saved changing variable loop affect operation loop however countervariable must changed loop operate normally first time statement executed counter value type initialvalue

beginning loop value countervariable compared finalvalue value countervariable greater finalvalue loop complete execution continue statement following next statement hand counter exceeded finalvalue control pass first statement statement increment negative number loop complete value countervariable less finalvalue

program flow reach next statement counter incremented specified increment amount decremented increment negative value step increment language included statement increment default

exit exit block prematurely

following script decrement beginning loop less


step
print



## FOR EACH IN / END FOR

item object next

statement iterate item object ifenum interface enumerator block terminated next statement object ordered intrinsically rolist enumerated order object intrinsic order roassociativearray enumerated apparent random order possible delete entry enumerated

exit exit block prematurely

following object enumerated rolist roarray roassociativearray romessageport

following script iterates associative array random order print keyvalue pair deletes


aajoe fred sue9

print naan
aadeleten



### Nesting FOR EACH Statements

statement track pointer object instance nesting loop iterate object cause series terminate prematurely


value

keyouter value
print outer keyouter valueskeyouter
keyinner value cause problematic behavior
print inner keyinner valueskeyinner




work around limitation associative array copy key array iterate array nested loop


value
valuesarray

value copy key array
valuesarraypushkey


keyouter value
print outer keyouter valueskeyouter
keyinner valuesarray iterate array key
print inner keyinner valueskeyinner




## WHILE / EXIT WHILE

expression exit

loop executes specified expression false exit statement exit block prematurely





print loop


true
print loop
exit



## IF / THEN / ELSE

expression statement else statement

note
singleline form else statement next section detail block form else statement

statement instructs interpreter test following expression expression true control proceed statement immediately following expression expression false control jump either matching else statement next program line block

##### **Example**


x127 print range


optional similar statement however sometimes required eliminate ambiguity following example


wont work without


## Block IF / ELSEIF / THEN / ENDIF

block multiline form else following syntax


booleanexpression
block
elseifstatement
elsestatement


elseifstatement
elseif booleanexpression
block

elsestatement
else
block


##### **Example**


vpmsgloop
msgwaittiut
typemsgrovideoevent
debug print video eventmsggetint
msggetint meden
debug print videofinished
retcode5
return
endif
else typemsgrogpiobutton
debug print button pressmsg
esc0 msgb0 retcode1return
esc1 msgb1 retcode2return
esc2 msgb2 retcode3return
esc3 msgb3 retcode4return
else typemsg invalid
debug print timeout
retcode6
return
endif

goto vpmsgloop


## Function() As Type / End Function

function nameparameter type type

note
function scope

function declared using function statement parenthesis contain optional parameter parameter also default value expression

type parameter declared return type function also declared parameter type return type declared dynamic default intrinsic type passed value copy made object passed reference statement used instead function shortcut creating function return type void

parameter following type

integer

float

double

string

object

dynamic


function return following type

void

integer

float

double

string

object

dynamic


#### "M" Identifier 

function called associative array local variable associative array function stored function called associative array variable associative array global module persists across call

identifier used purpose stated recommend using generalpurpose identifier

##### **Example**


main






objadd
print objresult


function void
mresultmamb
function


#### Anonymous Functions

function without name declaration considered anonymous

following simple anonymous function declaration


myfuncfunction
return
function

print myfunc12


anonymous function also used associativearray literal




starring functiono
egetbody
print starring
toks boxstrtokenize
toks
actx boxacttrim
actx
print actor actx
oactorspushactx
endif

return
function


qstarringmyobj myxml


developersdevelopersbrightscriptlanguagereferencereservedwordsmd
# Reserved Words



version older version

version

version

version

version

version

version

previous version




endsub linenum
createobject endwhile step
exit next stop
exitwhile
false objfun
else
function
endfor goto print true
endfunction type
endif invalid return

although strictly reserved word used identifier outside intended purposelanguagereferenceprogramstatementsmd

developersdevelopersbrightscriptlanguagereferencescopemd
# Scope



version older version

version

version

version

version

version

version

previous version


brightscript us following scoping rule

global variable supported however single hardcoded global variable global interface global brightscript objectbrightscriptobjectreferenceglobalfunctionsmd contains global library function

function declared function statement global scope however function anonymous still local scope

local variable exist within function scope function call another function function scope

label exist within function scope

block statement create separate scope

developersdevelopersbrightscriptlanguagereferencethreadingmodelmd
# Threading Model



version older version

version

version

version

version

version

version

previous version


brightscript run single thread general brightscript object call synchronous return quickly asynchronous take substantial amount time complete example method belonging roarray object synchronous play method part rovideoplayer object return immediately asynchronous video play rovideoplayer object post message message port indicating event medium playback finished frame reached

object implementer decides whether brightscript object launch background thread perform synchronous operation sometimes object feature synchronous asynchronous version method

threading model ensures script writer deal mutexes synchronization object script always single threaded message port polled waited receive event thread hand implementing brightscript object consider threading issue example rolist romessageport object threadsafe internally allowing used multiple thread

developersdevelopersbrightscriptlanguagereferencevariablesliteralsandtypesmd
# Variables, Literals, and Types



version older version

version

version

version

version

version

version

previous version




table content

identifiersidentifiers
examplesexamples
typestypes
type declaration characterstypedeclarationcharacters
literal constantsliteralsconstants
array literalsarrayliterals
associative array literalsassociativearrayliterals
invalid object returninvalidobjectreturn
numbersnumbers
dynamic typingdynamictyping
type conversiontypeconversion
type conversion accuracytypeconversionandaccuracy

## Identifiers

identifier name variable function label also apply brightscript object method function interface appear operator identifier following rule

must start alphabetic character

consist alphabetic character number underscore symbol

case sensitive

length

reserved wordlanguagereferencereservedwordsmd

variable optional type declaration string integer float double


##### **Examples**



boy5
superman



## Types

brightscript support dynamic typing declared type mean every value type determined runtime variable also instructed always contain value specified type value assigned variable specified type type value converted variable type possible conversion impossible runtime error occur

variable type declaration change type dynamically example statement create integer following statement specifying ahello change type variable string

brightscript support following type

boolean true false

integer 32bit signed integer number

float smallest floating point number format supported either hardware software

double largest floating point number format supported either hardware software although double intrinsically understood type implemented internally rointrinsicdouble object

string sequence ascii utf8 character brightscript us intrinsic string state

constant string statement sastring create intrinsic constant string

rostring instance string used expression becomes rostring instance example statement bstring cause intrinsic string convert rostring instance followed statement value reference copy behavior reference counting string brightscript version

object reference brightscript object native component note type function return object type object instead rolist rovideoplayer also note separate type intrinsic brightscript object intrinsic brightscript object built roassociativearray object type

interface interface brightscript object operator used interface type member must static since object context

invalid type value invalid type returned various instance type valid example indexing array never sent also assigned variable statement invalid


following example different type statement shortcut print type function return string identifies type passed expression


brightscript type1
integer

brightscript type10
float

brightscript typehello
string

brightscript typecreateobjectrolist
rolist

brightscript type1
integer

brightscript
brightscript typeb
float

brightscript chello
brightscript typec
string

brightscript dhello
brightscript typed
string

brightscript
brightscript typed
integer

brightscript
brightscript typed
float

brightscripteinvalid
brightscripttypee
invalid


## Type Declaration Characters

type declaration used variable literal type variable identifier separate type separate variable example defining would create independent variable



character type example
string
integer
singleprecision float
doubleprecision double

## Literals (Constants)

following valid literal type

type boolean either true false

type invalid invalid

type string string quote string

type integer integer decimal format

type float number decimal scientific notation 123456e30 float type designator

type double number scientific notation containing doubleprecision exponent symbol 123456789d12 double type declaration

type function similar variable formatting myfunction

type integer linenum current source line number


## Array Literals

array operator used declare array contain literal constant expression



myarray
myarray
myarray true


## Associative Array Literals

associative array operator used define associative array contain literal constant expression



key1value key2 key3


array associative array also defined following format



myfunc1 afunction
myval1 value



## Invalid Object Return

many method function return object also return invalid example case object return case variable accepting result must dynamically typed since assigned either type

following code return type mismatch string string type declaration thus cannot contain invalid



lpop


## Numbers

### Dynamic Typing

following rule determine integer double float dynamically typed

constant contains digit used exponent number double adding type declaration also force constant double

number double precision contains decimal point number float expressing number scientific notation using exponent also force constant float

neither condition true constant number integer


### Type Conversion

operation performed number result must typed integer float double addition subtraction multiplication operation performed result degree precision precise operand example multiplying integer double return number double

operand integer result integer number result integer operand outside 32bit range operation return carried double

division operates using rule except never carried integer level operator integer operation return carried float

comparison operation convert number type compared less precise type always converted precise type

### Type Conversion and Accuracy

float double number converted integer type rounded largest integer greater number used also happens function called number

double number converted float type rounded least significant digit rounded fractional part otherwise left unchanged

float number converted double type seven significant digit accurate

developersdevelopersbrightscriptlanguagereferencexmlsupportmd
# XML Support



version older version

version

version

version

version

version

version

previous version




table content

operatordotoperator
attribute operatorattributeoperator
examplesexamples
flikr code clipflikrcodeclip

brightscript provides support brightscript object dedicated language feature

roxmlelement object provides support parsing generating containing

roxmllist object used contain list roxmlelement instance


## Dot Operator

operatorlanguagereferenceoperatorsmd following feature used object

used roxmlelement instance operator return roxmllist instance child tag match operand tag match operand empty list returned

applied roxmllist instance operator aggregate result performing operation roxmlelement list

applied technically case sensitive operator still case insensitive wish perform casesensitive operation member function roxmlelementroxmllist object


## Attribute Operator

attribute operator used roxmlelement instance return named attribute though case sensitive attribute operator always case insensitive attribute operator used roxmllist instance return value list contains exactly element

## Examples


version10 encodingutf8
statok
photo page1 pages5 perpage100 total500
photo id3131875696 owner21963906n06 secretf248c84625 server3125
farm4 titlevny ispublic1 isfriend0 isfamily0
photo id3131137552 owner8979045n07 secretb22cfde7c4 server3078
farm4 titlehoot ispublic1 isfriend0 isfamily0
photo id3131040291 owner27651538n06 secretae25ff3942 server3286
farm4 title172 someone told ispublic1 isfriend0

photo



given examplexml file following code return roxmllist instance three entry


rspcreateobjectroxmlelement
rspparsereadasciifileexamplexml

rspphotosphoto


following return roxmlelement reference first photo id3131875696


rspphotosphoto0


following return roxmllist reference containing photo


rspphotos


following return string


rspphotosperpage


roxmlelementgettext method return element text example variable booklist contains element book langengthe dawn manbook following code print string dawn


print booklistbookgettext


alternatively using attribute operator print string


print booklistbooklang


### Flikr code clip



interestingness
pas optional page value photo
starting 0100200300400

return list interestingness photo entry



function getinterestingnessphotolisthttp object page1 integer object


print pagepage








rspcreateobjectroxmlelement
rspparsexml stop

return helperphotolistfromxml rspphotosphoto rspgetbodypeekgetbody


function


function helperphotolistfromxmlhttp object xmllist object ownerinvalid dynamic object


photolistcreateobjectrolist
photo xmllist
photolistpushnewphotofromxml photo owner

return photolist


function



newphotofromxml

take roxmlelement object photo photo
return object type photo
photogettitle
photogetid
photogeturl
photogetowner



function newphotofromxmlhttp object object owner dynamic object
photo createobjectroassociativearray
photo
photoxmlxml
photoownerowner
photogettitlefunctionreturn mxmltitleend function
photogetidfunctionreturn mxmlidend function
photogetownerpgetowner
photogeturlpgeturl
return photo
function


function pgetowner string
mownerinvalid return mowner
return mxmlowner
function


function pgeturl string
amxmlgetattributes

return
function


developersdevelopersbrightscriptlanguagereferencemd
# Language Reference



version older version

version

version

version

version

version

version

previous version


following general characteristic brightscript compared common scripting language

brightscript case sensitive

statement syntax similar python basic ruby dissimilar

like javascript object named dataentry structure associative array

brightscript support dynamic typing like javascript declared type like java

similar java brightscript us interface component object


brightscript code compiled bytecode interpreter compilation step occurs every time script loaded similar javascript separate compilation step result saved binary file

brightscript component architecture written speed efficiency portability since many embedded processor floatingpoint unit brightscript make extensive integer type unlike language including javascript brightscript us floating point number necessary

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsroarraymd
# roArray

object store object continuous array memory location since roarray contains brightscript component object wrapper intrinsic data type entry either different type type

object creation roarray object created parameter


createobjectroarray size integer resize boolean


size initial number entry allocated array

resize true array resized larger accommodate entry needed array large process might take time


dimbrightscriptlanguagereferenceprogramstatementsmd statement used instead createobject function create array statement advantageous automatically creates arrayofarray structure multidimensional array

## ifArray

##### Peek() As Dynamic

return last highest index array entry without removing

##### Pop() As Dynamic

return last highest index entry remove array

##### Push(entry As Dynamic)

add highestindex entry array

##### Shift() As Dynamic

remove index zero array shift entry unit

##### Unshift(entry As Dynamic)

add index zero array shift entry unit

##### Delete(index As Integer) As Boolean

deletes indicated array entry shift entry unit

##### Count() As Integer

return length array index highest entry array plus

##### Clear()

deletes every entry array

##### Append(array As roArray)

appends roarray another passed roarray contains entry never value appended

note
appended object must type

## ifEnum

##### Reset()

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true exact statement

## ifArrayGet

##### GetEntry(index As Integer) As Dynamic

return array entry given index entry start zero entry specified index method return invalid

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic)

set entry given index passed type value

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsroassociativearraymd
# roAssociativeArray

object allows store object associative array also known dictionary hash table data structure associate object string key

note
using nested loop iterate roassociativearray instance lead unexpected behavior statement descriptionbrightscriptlanguagereferenceprogramstatementsmd detail

roassociativearray object created parameter


createobjectroassociativearray


alternatively associative array created using bracket



key1value key2 key3


## ifEnum

##### Reset() As Void

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true associative array contains element

## ifAssociativeArray

##### AddReplace(key As String, value As Object) As Void

add entry associative array associating supplied object supplied string object associated existing object linked discarded method always casesensitive creating key whereas objectliteral syntax aabrightsign caseinsensitive creating key unless setmodecasesensitive called

##### Lookup(key As String) As Dynamic

look specified return associated object object associated string method return invalid



many case operatorbrightscriptlanguagereferenceoperatorsmd used shorthand lookup addreplace method working associative array

##### DoesExist(key As String) As Boolean

look specified associative array exists true returned otherwise false returned

##### Delete(key As String) As Boolean

look object associative array linked specified object deleted true returned otherwise false returned

##### Clear() As Void

remove object associative array

##### SetModeCaseSensitive() As Void

make subsequent action case sensitive lookup created key exception addreplace method case insensitive default

##### LookupCi(key As String) As Dynamic

look object array associated specified method function similarly lookup exception comparison always case insensitive regardless case mode

##### Append(aa As roAssociativeArray) As Void

appends second associative array first

## Examples


createobjectroassociativearray
aaaddreplacebright sign
aaaddreplacetmol
print aalookuptmol
print aalookupbright


script return following



sign


alternatively operatorbrightscriptlanguagereferenceoperatorsmd place addreplace lookup method



aabright sign
aatmol
print aatmol
print aabright


also specify associative array multiline object literal



bright sign
tmol





developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrobooleanmd
# roBoolean

object equivalent boolean intrinsic type useful following situation

object needed instead intrinsic value example boolean added rolist automatically wrapped roboolean object language interpreter function expects brightscript component parameter passed boolean brightscript automatically creates equivalent brightscript component

object expose ifboolean interface object used expression expects intrinsic value


## ifBoolean 

##### GetBoolean() As Boolean

##### SetBoolean(a As Boolean

#####

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrobytearraymd
# roByteArray

object contains function converting string byte array well ascii ascii base64

note
converting byte array string byte array contains zero string conversion point

byte array automatically resize become larger needed wish disable behavior setresize method uninitialized index read invalid returned

since robytearray support ifarray interface accessed array operator byte array always accessed unsigned byte interface used object also support ifenum interface used statement

javascript equivalent blob note javascript typed array example uint8array

## ifByteArray

##### WriteFile(file\_path As String) As Boolean

writes byte contained byte array specified file method return true successful

##### WriteFile(file\_path As String, start\_index As Integer, length As Integer) As Boolean

writes subset byte contained byte array specified file method writes length byte beginning startindex byte array

##### ReadFile(file\_path As String) As Boolean

read specified file byte array operation discard data currently contained byte array

##### ReadFile(file\_path As String, start\_index As Integer, length As Integer) As Boolean

read section specified file byte array method read length byte beginning startindex file operation discard data currently contained byte array

##### AppendFile(file\_path As String) As Boolean

appends content byte array specified file

##### SetResize(minimum\_allocation\_size As Integer, autoresize As Boolean)

expands size byte array minimumallocationsize less minimumallocationsize method also accepts boolean parameter specifies whether byte array resized automatically

##### ToHexString() As String

return hexadecimal string representation content byte array byte represented digit

##### FromHexString(hex\_string As String)

writes content passed hexadecimal string byte array passed string must contain even number digit operation discard data currently contained byte array

##### ToBase64String() As String

return content byte array base64formatted string

##### FromBase64String(base\_64\_string As String)

writes content valid base64formatted string byte array operation discard data currently contained byte array

##### ToAsciiString() As String

return content byte array asciiformatted string

##### FromAsciiString(ascii\_string As String)

writes content valid asciiformatted string byte array operation discard data currently contained byte array

##### GetSignedByte(index As Integer) As Integer

return signed byte specified zerobased index byte array read unsigned byte within byte array ifarraygetgetentry method array operator

##### GetSignedLong(index As Integer) As Integer

retrieves integer located specified longword index byte array note method cannot accept byte index parameter

##### IsLittleEndianCPU() As Boolean

return true architecture littleendian

## ifArray

##### Peek() As Dynamic

return last highest index array entry without removing

##### Pop() As Dynamic

return last highest index entry remove array

##### Push(entry As Dynamic)

add highest index entry array

##### Shift() As Dynamic

remove index zero array shift entry unit

##### Unshift(entry As Dynamic)

add index zero array shift entry unit

##### Delete(index As Integer) As Boolean

deletes indicated array entry shift entry unit

##### Count() As Integer

return index highest entry array plus length array

##### Clear()

deletes every entry array

##### Append(array As roArray)

appends roarray another passed roarray contains entry never value appended

note
appended object must type

## ifEnum

##### Reset()

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true exact statement

## ifArrayGet

##### GetEntry(index As Integer) As Dynamic

return array entry given index entry start zero method attempt fetch entry return invalid

## ifArraySet

##### SetEntry(index As Integer, entry As Dynamic)

set entry given index passed type value

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrodoublerointrinsicdoublemd
# roDouble, roIntrinsicDouble

## ifDouble

##### GetDouble() As Double

##### SetDouble(a As Double)

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrofunctionmd
# roFunction

## ifFunction

##### GetSub() As Function

##### SetSub(value As Function)

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrointrofloatrostringmd
# roInt, roFloat, roString

intrinsic type int32 float string object interface equivalent useful following situation

object needed instead typed value rolist object maintains list object function expects brightscript object parameter passed integer float string brightscript automatically creates equivalent object

object expose ifint iffloat ifstring interface object used expression expects typed value example rovideoeventobjectreferencepresentationandwidgetobjectsrovideoeventroaudioeventmd used integer value representing event


integer operation

type roint statement following effect

print print value ogetint

assigns integer value ogetint

presumably automatically typed becomes another reference roint

osetint5 instead release change type roint32 automatically typed assigns


## ifInt

roint contains ifint interface provides following

##### GetInt() As Integer

return integer value object

##### SetInt(value As Integer) As Void

set integer value object

## ifIntOps

roint also contains ifintops interface provides following

##### ToStr() As String

return integer value string space appended front positive number

## ifFloat

rofloat contains iffloat interface provides following

##### GetFloat() As Float

return float value object

##### SetFloat(value As Float) As Void

set float value object

## ifString

rostring contains ifstring interface provides following

##### GetString() As String

return string value object

##### SetString(value As String) As Void

set string value object

## ifStringOps

rostring also contains ifstringops interface provides following

note
global functionsobjectreferenceglobalfunctionsmd offer functionality ifstringops method function index ifstringops method start zero global function start

##### SetString(str As String, str\_len As Integer)

set string value object using specified string stringlength value similar setseting method accept parameter string length

##### AppendString(str As String, str\_len As Integer)

appends string value object using specified string stringlength value method modifies itselfthis cause unexpected result pas intrinsic string type rather string object

##### **Example**


xstring
xifstringopsappendstringddd3
print print string
yboxstring
yifstringopsappendstringddd3
print print stringddd


##### Len() As Integer

return number character string

##### GetEntityEncode() As String

return string certain character replaced html entity encoding sequence

character replaced

double quote quot
single quote apos




##### Tokenize(delim As String) As roList

split string substring using specified delimiter character delim parameter contain character treat delimiters string object contains multiple contiguous delimiters treated single delimiter method return substring rolist object delimiters returned substring

##### **Example**


brightscript onetwo
brightscript print stokenize




##### Trim() As String

return string leading trailing whitespace character nobreak space removed

##### ToInt() As Integer

return value string integer number

##### ToFloat() As Float

return value string floating point number

##### Left(n As Integer) As String

return first character string

##### Right(n As Integer) As String

return last character string

##### Mid(start\_index As Integer) As String

return subset string begin zerobased startindex terminates string

##### Mid(start\_index As Integer, n As Integer) As String

return subset string beginning zerobased startindex consisting character string contains fewer character specified startindex method return character startindex

##### Instr(substring As String) As Integer 

return zerobased index first occurence substring string substring occur string method return

##### Instr(start\_index As Integer, substring As String) As Integer

return zerobased index first occurence substring specified startindex string substring occur specified startindex method return



instr also offered global functionobjectreferenceglobalfunctionsmd note string index global function start

## Examples


brightscript ocreateobjectroint
brightscript osetint555
brightscript print

brightscript print ogetint

brightscript print



integer value converted type roint automatically addtail method expects brightscript object parameter


brightscript listcreateobjectrolist
brightscript listaddtail5
brightscript print typelistgettail


listdir method return rolist object containing rostring object


brightscript llistdir
brightscript lcountprint lremoveheadnext
testmovie3vob
testmovie4vob
testmovie1vob
testmovie2vob


developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrojremd
# roJRE

object allows load java application using java runtime environment player java runtime longer built firmware rojre invokable unless bsfw file extension player install must invoke rojre contact brightsign customer support bsfw file extension

us openjdk available xtx4443 xdx3433 hdx2423 ls424423 4kx42 model

object creation rojre object instantiated java package filename optional associative array specifies system property program argument type global function determine package successfully loaded


createobjectrojre filename string option roassociativearray


associative array contain entry

defines associative array specifying system property

argument array specifying commandline argument


propertyargument value must passed string note associativearray key case insensitive converted lowercase default roassociativearraysetmodecasesensitive method enable casesensitive key

##### **Example**


prop
propssetmodecasesensitive
propssysprop1 system prop
propssysprop2 system prop
propsjavaiotmpdir vartmp

createobjectrojre appjar defines prop argument
typejrerojre
print successfully started java runtime
else
print unable start java runtime



developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsrolistmd
# roList

object function generalpurpose doubly linked list used container arbitrarylength list brightsign object array operator used access element ordered list

## ifList

##### Count() As Integer

return number element list

##### ResetIndex() As Boolean

reset current index position list head element

##### AddTail(obj As Object) As Void

add typed value tail list

##### AddHead(obj As Object) As Void

add typed value head list

##### RemoveIndex() As Object

remove entry list current index position increment index position list return invalid list reached

##### GetIndex() As Object

retrieves entry list current index position increment index position list return invalid list reached

##### RemoveTail() As Object

remove entry tail list

##### RemoveHead() As Object

remove entry head list

##### GetTail() As Object

retrieves entry tail list keep entry list

##### GetHead() As Object

retrieves entry head list keep entry list

##### Clear()

remove element list

## ifEnum

##### Reset()

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true exact statement

## ifArray

##### Peek() As Dynamic

return last highest index list entry without removing

##### Pop() As Dynamic

return last highest index entry remove list

##### Push(entry As Dynamic)

add highestindex entry list

##### Shift() As Dynamic

remove index zero list shift entry unit

##### Unshift(entry As Dynamic)

add index zero list shift entry unit

##### Delete(index As Integer) As Boolean

deletes indicated list entry shift entry unit

##### Count() As Integer

return length list index highest entry list plus

##### Clear()

deletes every entry list

##### Append(list As roList)

appends rolist another passed rolist contains entry never value appended

note
appended object must type

## ifArrayGet 

##### GetEntry(a As Integer) As Dynamic

return list entry given index entry start zero entry fetched invalid returned

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic)

set entry given index passed type value

## Example


list createobjectrolist
listaddtaila
listaddtailb
listaddtailc
listaddtaild
listresetindex
listgetindex
invalid
print
listgetindex

print list2


developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsromessageportmd
# roMessagePort

message port destination message event sent explanation event loopsobjectreferencemd detail call function directly using brightscript instead wait global functionobjectreferenceglobalfunctionsmd

## ifMessagePort

##### GetMessage() As Object

return event object available otherwise invalid returned either case method return immediately without waiting

##### WaitMessage(timeout As Integer) As Object

wait event object available specified amount millisecond passed event object becomes available returned timeout reached invalid returned passing zero timeout value instructs method wait indefinitely message

also wait global function retrieve event object specified interval following statement effect


portwaitmessagetimeout
waittimeout port


##### PostMessage(msg As Object) As Void  


##### PeekMessage() As Object

return event object available invalid otherwise remove event object message queue later call getmessage waitmessage peekmessage return event object

##### SetWatchdogTimeout(seconds As Integer) As Integer

enables watchdog timeout romessageport instance passed positive integer watchdog crash reboot player script call getmessage waitmessage specified number second timeout blocked script wait message port passing zero method disables watchdog

brightscript operation roassetrealizerrealize take long time return case better short watchdog timeout general switch longer timeout calling operation

watchdog timeout applies associated romessageport instance enabling watchdog romessageport instance calling waitmessage another cause watchdog trigger unexpectedly watchdog trigger waiting brightscript debugger prompt

##### DeferWatchdog(seconds As Integer)

defers watchdog timeout setwatchdogtimeout method passing integer method defers timeout specified number second

##### DeferWatchdog()

defers watchdog timeout amount second setwatchdogtimeout method

note
call either deferwatchdog method cannot cause watchdog trigger earlier already example calling deferwatchdog100 followed deferwatchdog10 still cause watchdog trigger second

## ifEnum

##### Reset()

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true next element

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsroregexmd
# roRegex

object allows implementation regularexpression processing provided pcre library javascript equivalent regexp

object created string represent matchingpattern string indicate flag modify behavior matching operation


createobjectroregex


match string example match lowercase letter include perl compatible regular expression found pcre documentation

object support combination following behavior flag example modified match uppercase lowercase letter

caseinsensitive match mode

multiline mode startline endline construct match immediately newline subject string also match absolute beginning string

dotall mode includes newline regular expression modifier equivalent perl

extended mode ignores whitespace character except escaped inside character class modifier equivalent perl


## ifRegex

##### IsMatch(string As String) As Boolean

return true string consistent matching pattern

##### Match(string As String) As roArray

return roarray matched substring string entire match returned form array0this entry array parenthetical substring matching pattern contains parenthetical substring relevant substring returned array length array0 entire match additional entry array match corresponding parenthetical expression

##### Replace(string As String, subset As String) As String

replaces first occurrence matching pattern string subset return result

subset contain numbered backreferences parenthetical substring

##### **Example**


createobjectroregex
rreplace123 word2 number1
wordabc number123


##### ReplaceAll(string As String, subset As String) As String

replaces occurrence matching pattern string subset return result

##### **Example**


createobjectroregex
rreplaceallabracadabra
xbrxcxdxbrx


##### Split(string As String) As roList

us matching pattern delimiter split string delimiter boundary function return rolist string separated matching pattern original string

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsroxmlelementmd
# roXMLElement

object used contain tree javascript equivalent domparser

roxmlelement object created parameter


createobjectroxmlelement


following example illustrate element parsed brightscript


tag1this example texttag1


name tag1

attribute invalid

body rostring containing example text



tag2 cavemanbarney


name tag2

attribute roassociativearray entry caveman barney

body invalid


contains tag body type roxmllist

generate content create roxmlelement call setbody setname method build itthen call genxml method generate

##### **Example**


rootsetnamemyroot
rootaddattributekey1value1
rootaddattributekey2value2
nerootaddbodyelement
nesetnamesub
nesetbodythis sub1 text
nerootaddbodyelement
nesetnamesubelement2
nesetbodymore text
neaddattributekv
nerootaddelementsubelement3
nesetbodymore text
rootaddelementwithbodysubanother
printxmlroot
print rootgenxmlfalse


## ifXMLElement

##### GetBody() As Object  


##### GetAttributes() As Object  


##### GetName() As String  


##### GetText() As String  


##### GetChildElements() As Object  


##### GetNamedElements(a As String) As Object  


##### GetNamedElementsCi(a As String) As Object  


##### SetBody(a As Object)

generates roxmllist body needed method add passed item roxmlelement

##### AddBodyElement() As Object  


##### AddElement(a As String) As Object  


##### AddElementWithBody(a As String, b As Object) As Object  


##### AddAttribute(a As String, b As String)  


##### SetName(a As String)  


##### Parse(a As String) As Boolean

parses content passed event failure method return false however also populates roxmlelement whatever text could successfully parsed avoid passing along erroneous string always best script check return value parse using

##### GenXML(a As Boolean) As String

generates content method take single boolean parameter indicating whether

##### Clear() As Void  


##### GenXMLHdr(a As String) As String  


##### IsName(a As String) As Boolean  


##### HasAttribute(a As String) As Boolean  


##### ParseFile(a As String) As Boolean

## Example

subroutine example print content roxmlelement tree


printxmlroot

printxmlelement object depth integer
print tabdepth3name elementgetname
elementgetattributesisempty
print tabdepth3attributes
elementgetattributes
print aleftelementgetattributesa
elementgetattributesisnext print

print

elementgettextinvalid
print tabdepth3contains text leftelementgettext

elementgetchildelementsinvalid
print tabdepth3contains roxmllist
elementgetchildelements
printxmle depth1


print



developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsroxmllistmd
# roXMLList

javascript equivalent object domparser

## ifXMLList

##### Simplify() As Object

return roxmlelement list contains exactly element otherwise return

##### GetAttributes() As Object  


##### GetText() As String  


##### GetChildElements() As Object  


##### GetNamedElements(a As String) As Object

return xmllist contains roxmlelements match name passed element action using operator roxmllist

##### GetNamedElementsCi(a As String) As Object

## ifList

##### Count() As Integer

return number element list

##### ResetIndex() As Boolean

reset current index position list head element

##### AddTail(obj As Object) As Void

add typed value tail list

##### AddHead(obj As Object) As Void

add typed value head list

##### RemoveIndex() As Object

remove entry list current index position increment index position list return invalid list reached

##### GetIndex() As Object

retrieves entry list current index position increment index position list return invalid list reached

##### RemoveTail() As Object

remove entry tail list

##### RemoveHead() As Object

remove entry head list

##### GetTail() As Object

retrieves entry tail list keep entry list

##### GetHead() As Object

retrieves entry head list keep entry list

##### Clear() As Void

remove element list

## ifEnum

##### Reset()

reset position first element enumeration

##### Next() As Dynamic

return typed value current position increment position

##### IsNext() As Boolean

return true next element

##### IsEmpty() As Boolean

return true exact statement

## ifArray

##### Peek() As Dynamic

return last highest index array entry without removing

##### Pop() As Dynamic

return last highest index entry remove array

##### Push(a As Dynamic)

add highest index entry array

##### Shift() As Dynamic

remove index zero array shift entry unit

##### Unshift(a As Dynamic)

add index zero array shift entry unit

##### Delete(a As Integer) As Boolean

deletes indicated array entry shift entry unit

##### Count() As Integer

return index highest entry array plus length array

##### Clear() As Void

deletes every entry array

##### Append(a As Object) As Void

appends roarray another passed roarray contains entry never value appended

note
appended object must type

## ifArrayGet 

##### GetEntry(a As Integer) As Dynamic

return array entry given index entry start zero entry fetched invalid returned

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic) As Void

set entry given index passed type value

developersdevelopersbrightscriptobjectreferencebrightscriptcoreobjectsmd
# BrightScript Core Objects



version older version

version

version

version

version

version

version

previous version


section describes object provide core brightscript functionality

roarraybrightscriptcoreobjectsroarraymd
roassociativearraybrightscriptcoreobjectsroassociativearraymd
robooleanbrightscriptcoreobjectsrobooleanmd
robytearraybrightscriptcoreobjectsrobytearraymd
rodouble rointrinsicdoublebrightscriptcoreobjectsrodoublerointrinsicdoublemd
rofunctionbrightscriptcoreobjectsrofunctionmd
roint rofloat rostringbrightscriptcoreobjectsrointrofloatrostringmd
rojrebrightscriptcoreobjectsrojremd
rolistbrightscriptcoreobjectsrolistmd
romessageportbrightscriptcoreobjectsromessageportmd
roregexbrightscriptcoreobjectsroregexmd
roxmlelementbrightscriptcoreobjectsroxmlelementmd
roxmllistbrightscriptcoreobjectsroxmllistmd

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetcollectionmd
# roAssetCollection

object used represent collection asset

object creation roassetcollection object created parameter


createobjectroassetcollection


populate asset collection individual call addasset addassets also populate asset collection using rosyncspecgetassets method shown


assetcollection createobjectroassetcollection

localcurrentsync createobjectrosyncspec
localcurrentsyncreadfromfilelocalsyncxml
assetcollection localcurrentsyncgetassetsdownload
endif


## ifFailureReason

##### GetFailureReason() As String

return additional information method fails

## ifAssetCollection 

##### AddAsset(asset\_info As Dynamic) As Boolean

add single asset associative array jsonformatted string argument string match format used single asset json sync spec return true indicate success false indicate failure false returned detailed information available calling getfailurereason method

##### AddAssets(asset\_info\_array As Dynamic) As Boolean

add multiple asset enumerable object rolist roarray string containing jsonformatted array contains compatible associative array return true indicate success false indicate failure false returned detailed information available calling getfailurereason method

##### GetAssetList() As roList

return rolist instance containing associative array asset metadata method efficient therefore recommended debugging diagnostic purpose

associative array contains following



name string required name asset file realized must valid filename slash
link string required download location asset
size integerstring optional size asset string want specify number large integer allows file size larger
hash string optional string form hashalgorithmhash next table available hash algorithm
changehint string optional string change conjunction file content necessary link hash supplied always change
authinherit boolean optional indication whether asset us roassetfetcher authentication information default true
authuser boolean optional user utilize authentication downloading asset automatically disables authinherit
authpassword boolean optional password downloading asset automatically disables authinherit
headersinherit boolean optional command pas header supplier roassetfetcher fetching asset default true

caution
important
optional field specified populating pool must also specified retrieving asset pool become mandatory used asset example hash value specified fetching pool must also specified attempting refer file pool

hash algorithm



sha1 sha1 available validate hash file downloaded hash available used link changehint property effect pool file name file shared even downloaded different location
besha1 algorithm hash file along file size order verify content also move link changehint property pool filename
us hash algorithm validate file
none without hash file cannot verified downloaded system rely link changehint property give pool unique filename

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetfetchermd
# roAssetFetcher

object contains function downloading file pool javascript equivalent assetpoolfetcherdevelopersplayerapisjavascriptapisassetfetchermd

object creation roassetfetcher object must passed roassetpool instance upon creation


createobjectroassetfetcher pool roassetpool


##### **Example**


pool createobjectroassetpool pool
fetcher createobjectroassetfetcher pool


## ifAssetFetcher

##### GetFailureReason() As String

return error string roassetfetcher method failed usually indicated returning false error string help diagnose failure

##### SetUserAndPassword(user As String, password As String) As Boolean

set default user password string used download request otherwise marked using following attribute auth inheritno auth useruser password password

##### EnableUnsafeAuthentication(enable As Boolean) As Boolean

support basic http authentication true http authentication us insecure protocol might allow others easily determine password roassetfetcher object still prefer stronger digest http supported server method false default setting refuse provide password basic http authentication request requiring authentication fail

##### EnableUnsafeProxyAuthentication(enable As Boolean) As Boolean

support basic http authentication proxy true unlike enableunsafeauthentication default setting http authentication us insecure protocol might allow others easily determine password method false refuse provide password basic http authentication request requiring authentication type fail

##### EnableEncodings(enable As Boolean) As Boolean

enables http compression communicates server system accept encoding roassetfetcher object capable decoding behavior enabled default supported encoding currently include deflate gzip allow transparent compression response client roassetfetcher instance decoded data unaware encoding used

##### AsyncDownload(assets As roAssetCollection) As Boolean

begin populating asset pool using file listed passed roassetcollection instance file already pool downloaded automatically event raised download process indicate whether individual file downloads succeeded failed finally single event raised indicating whether entire asset collection downloaded successfully roassetfetcherevent roassetfetcherprogressevent entry detail

##### AsyncSuggestCache(spec As roAssetCollection) As Boolean 

begin downloading required file passed roassetcollection instance disconnect shortly afterward player suitably configured proxy either globally setproxy method proxy continue download file making readily available asyncdownload call future

method generates roassetfetcherevent message response code accepted indicate success error reported usual final allfilescomplete event code always eventallfailed download complete

##### AsyncCancel() As Boolean

cancel pending async request note prior method call event associated asynchronous action queued event queued call return recommend collecting pending event prior calling async method object avoid confusion

##### EnablePeerVerification(verification As Boolean) As Boolean

enables checking tlsssl certificate method true default disabling peer verification allows bypass expired certificate check

##### EnableHostVerification(verification As Boolean) As Boolean

enables checking tlsssl certificate correct hostname method true default disabling host verification allows accept certificate sent wrong hostname

caution
important
peer verficiation host verification important security check prevent maninthemiddle attack feature disabled careful consideration security implication

##### SetCertificatesFile(filename As String) As Boolean

configures alternative certificate connection method useful connection certificate signed default trusted list example organization us private hierarchy signed well known root method replaces default list passed certificate file must contain acceptable certificate required connection

##### AddHeader(name As String, value As String) As Boolean

specifies header passed http request made roassetfetcher instance particular download include header header inheritno attribute sync spec

##### SetHeaders(headers As roAssociativeArray) As Boolean

specifies header passed http request made roassetfetcher instance method remove previously header particular download include header header inheritno attribute sync spec

##### SetProxy(proxy As String) As Boolean

set name address proxy server used roassetfetcher instance proxy string formatted contain four character character used replace octet current address example address currently 19216812 proxy proxy player attempt proxy named proxy192168

##### SetProxyBypass(hostnames As Array) As Boolean

exempts specified host proxy setting passed array consist hostnames roassetfetcher instance attempt reach specified host directly rather using proxy specified setproxy method example hostname would exempt proxy setting

##### SetFileProgressIntervalSeconds(interval As Integer) As Boolean

specifies interval second progress event individual file downloaded setting interval disables progress event setting interval specifies event generated often possible though slow transfer process interval positive integer event always generated start file download irrespective elapsed time default interval second

##### SetFileRetryCount(count As Integer) As Boolean

specifies maximum number time file download retried moving next file download default retry count five

##### SetRelativeLinkPrefix(prefix As String) As Boolean

specifies prefix appended front relative link sync spec normally method used make file uris drive agnostic also used reduce size sync spec file stored place nonrelative link affected method

##### BindToInterface(interface As Integer) As Boolean

ensures http request go specified network interface ethernet wifi default behavior specified passing send request using appropriate network interface depend routing metric configured ronetworkconfiguration object interface layer network method work expected linux weakhost model

##### SetMaximumReceiveBytesPerSecond(bytes\_per\_second as Double) As Boolean

limit rate downloads performed roassetfetcher instance source data rate isnt direct control brightsign player download rate average specified value time

method return true success false failure event failure getfailurereason method provide information

##### SetMinimumTransferRate(bytes\_per\_second As Integer, period\_in\_seconds As Integer) As Boolean

set minimum transfer rate file download transfer terminated rate drop bytespersecond averaged periodinseconds note transfer internet want periodinseconds small number case network problem cause temporary drop performance large file transfer small bytespersecond limit averaging fifteen minute appropriate

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type roassetfetcherevent roassetfetcherprogressevent attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetfetchereventmd
# roAssetFetcherEvent

event generated roassetfetcher instance file transfer succeeds fails population asset pool whole succeeds fails

## ifAssetFetcherEvent

##### GetEvent() As Integer

return integer indicating result roassetfetcher download attempt

pooleventfiledownloaded

pooleventfilefailed

pooleventalldownloaded

pooleventallfailed


##### GetName() As String

return filename associated event

##### GetFailureReason() As String

return additional failure information associated event

##### GetFileIndex() As Integer

retrieves zerobased index sync spec file associated event

##### GetResponseCode() As Integer

return protocol response code associated event following code indicate success

successful http transfer

successful transfer

successful local file transfer


unexpected error return value negative many possible negative error curl library often best look text version calling getfailurereason

potential error generated brightsign player



status name description
curleunsupportedprotocol
curlefailedinit
curleurlmalformat
curlecouldntresolveproxy
curlecouldntresolvehost
curlecouldntconnect
curleftpweirdserverreply
curleremoteaccessdenied service denied server lack access login fails returned
curleftpweirdpassreply
curleftpweirdpasvreply
curleftpweird227format
curleftpcantgethost
curleftpcouldntsettype
curlepartialfile
curleftpcouldntretrfile
curlequoteerror failed quote command
curlehttpreturnederror
curlewriteerror
curleuploadfailed failed upload command
curlereaderror could openread file
curleoutofmemory
curleoperationtimedout timeout time reached
curleftpportfailed port operation failed
curleftpcouldntuserest rest command failed
curlerangeerror range command work
curlehttpposterror
curlesslconnecterror wrong connecting
curlebaddownloadresume could resume download
curlefilecouldntreadfile
curleldapcannotbind
curleldapsearchfailed
curlefunctionnotfound
curleabortedbycallback
curlebadfunctionargument
curleinterfacefailed curloptinterface failed
curletoomanyredirects catch endless redirect loop
curleunknowntelnetoption user specified unknown option
curletelnetoptionsyntax malformed telnet option
curlepeerfailedverification peer certificate fingerprint wasnt verified correctly
curlegotnothing specific error
curlesslenginenotfound crypto engine found
curlesslenginesetfailed cannot crypto engine default
curlesenderror failed sending network data
curlerecverror failure receiving network data
curlesslcertproblem problem local certificate
curlesslcipher could specified cipher
curlesslcacert problem cert path
curlebadcontentencoding unrecognized transfer encoding
curleldapinvalidurl invalid ldap
curlefilesizeexceeded maximum file size exceeded
curleusesslfailed requested level failed
curlesendfailrewind sending data requires rewind failed
curlesslengineinitfailed failed initialize engine
curlelogindenied user password similar field accepted login failed
curletftpnotfound file found server
curletftpperm permission problem server
curleremotediskfull disk space server
curletftpillegal illegal tftp operation
curletftpunknownid unknown transfer
curleremotefileexists file already exists
curletftpnosuchuser user
curleconvfailed conversion failed
curleconvreqd caller must register conversion callback using following urleasysetopt option curloptconvfromnetworkfunction curloptconvtonetworkfunction curloptconvfromutf8function
curlesslcacertbadfile could load cacert file missing wrong format
curleremotefilenotfound remote file found
curlessh error layer somewhat generic error message important occurs
curlesslshutdownfailed failed shut connection

following error code generated system software outside range curl event



status name description
1002 enoent specified file exist cannot created
10001 cancelled operation cancelled
10002 exception operation caused local exception call getfailurereason detail
10003 errorexception unexpected exception occurred
10004 errordiskerror disk error occurred usually result disk full
10005 errorpoolunsatisfied expected file present pool
10006 errordownloadingelsewhere file downloaded another roassetfetcher instance
10007 errorhashmismatch downloaded file match checksum file size

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetfetcherprogresseventmd
# roAssetFetcherProgressEvent

event generated roassetfetcher object regular interval file downloads roassetfetchersetfileprogressintervalseconds method customize often progress event generated

## ifAssetFetcherProgressEvent

##### GetFileName() As String

return name file associated event file name retrieved sync spec associated roassetfetcher generated event

##### GetFileIndex() As Integer

return zerobased index sync spec file associated event

##### GetFileCount() As Integer

return total number file within sync spec

##### GetCurrentFileTransferredMegabytes() As Integer

return number transferred megabyte belonging file associated event

##### GetCurrentFileSizeMegabytes() As Integer

return size file associated event

##### GetCurrentFilePercentage() As Float

return floatingpoint number representing download percentage file associated event

note
file sizepercentage returned method derived asset size associated roassetcollection sync specnot http contentlength header specifying asset size zero cause method return zero

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetpoolmd
# roAssetPool

roassetpool instance represents pool file synchronization instruct object populate pool based sync spec realize specified directory required javascript equivalent assetpool

object creation roassetpool object created single parameter representing rooted path pool


createobjectroassetpool poolpath string


example


pool createobject roassetpool sdpool


## ifAssetPool

##### GetFailureReason() As String  


##### ProtectAssets(name As String, collection As Object) As Boolean

request file specified download section sync spec receive certain amount protection specified file deleted system software need reduce size pool make space

##### UnprotectAssets(name As String) As Boolean

remove protected status placed specified file protectassets method asset collection reference counted systemsoftware level result calling unprotectassets must pas object previously passed protectassets

##### UnprotectAllAssets() As Boolean

remove protected status placed file asset pool using protectassets method

##### ReserveMegabytes(size As Integer) As Boolean

reserve specified amount storage space method dynamic system software attempt keep space free even parallel process filling storage

##### SetMaximumPoolSizeMegabytes(maximum\_size As Integer) As Boolean

specifies maximum size roassetpool instance megabyte method resourceintensive reservemegabytes useful creating multiple pool storage device

##### GetPoolSizeInMegabytes() As Integer

return current size asset pool megabyte

##### Validate(sync\_spec As Object, options As roAssociativeArray) As Boolean

check sha1 besha1 hash value file sync spec currently present pool method return true check pas false check fail calling getfailurereason return information corrupt file note true return mean file sync spec currently present pool second parameter represents table validation option specifies option value specifies whether option enabled boolean value currently option deletecorrupt determines whether method automatically delete corrupt file

##### QueryFiles(sync\_spec As roAssociativeArray) As roAssociativeArray

determines whether specified file present asset pool method return associative array filename key corresponding boolean value

##### AssetsReady(collection As Object) As Boolean

return true specified file ready asset pool

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetpoolfilesmd
# roAssetPoolFiles

object allows interacting file asset pool javascript equivalent assetpoolfilesdevelopersplayerapisjavascriptapisassetpoolfilesmd

object creation roassetpoolfiles object created parameter


createobjectroassetpoolfiles pool roassetpool asset dynamic


asset argument either roassetcollection rosyncspec object multiple object instance requires roassetcollection instance efficient convert rosyncspec roassetcollection calling getassets passing collection object instance requiring

object work similarly rosyncpoolfiles object

## ifAssetPoolFiles

##### GetFailureReason() As String

return explanatory text getpoolfilepath return empty string getpoolfileinfo return invalid

##### MoveFileIntoPool(source\_filename As String, asset\_name As String) As Boolean

move arbitrary file appropriate location asset pool source file must filesystem asset pool method accepts parameter

sourcefilename string path existing file filesystem

assetname string name asset within asset collection associated roassetpoolfiles instance asset size known checked source file move operation fail assetname match asset pool file size match known asset size


method return true success false failure getfailurereason method retrieve error description

##### GetPoolFilePath(asset\_name As String) As String

look specified file name asset collection us information determine actual name file pool method return empty string name found asset collection file found pool

##### GetPoolFileInfo(asset\_name As String) As Object

look specified file name asset collection return available information including pool file path associative array method return invalid asset name found asset collection file found pool information asset collection returned without pool path table description asset associative array



field value description
name string asset name
link string asset
size string
hash string hash algorithm hash format
changehint string present
authuser string present
authpassword string present
authinherit boolean
headersinherit boolean
probe string probe data
path string absolute path file pool invalid file pool

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetrealizermd
# roAssetRealizer

object contains function realizing file extracting file asset pool placing standard file directory realizing complete asset pool recommended process slow instead script retrieve pool file location using roassetpoolfiles object refer file directly roassetrealizer object still useful realizing file must root directory work autorun firmware update file javascript equivalent assetrealizer

object creation roassetrealizer object requires parameter upon creation roassetpool object destination directory


createobjectroassetrealizer pool roassetpool destinationdirectory string


##### **Example**


pool createobjectroassetpool pool
realizer createobject roassetrealizer pool


## IfUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifAssetRealizer

##### GetFailureReason() As String

yield additional useful information function return indicates error

##### EstimateRealizedSizeInMegabytes(spec As Object) As Integer

return estimated amount space would taken specified sync spec

##### Realize(spec As roSyncSpec/roAssetCollection) As roAssetRealizerEvent

place file destination directory specified passed rosyncspec roassetcollection pool contain full required file method immediately fail file changed method attempt much work possible destructively modifying file system method automatically check length file hash match specification mismatch affected file deleted realization fails method indicates success failure returning roassetrealizerevent object

note
pool destination must file system

##### ValidateFiles(spec As Object, options As Object) As roAssociativeArray

check hash every file spec corresponding file destination path return associative array containing mismatched file name mapped reason option parameter roassociativearray currently support single option

deletecorrupt automatically deletes file match expected hash default file deleted

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetrealizereventmd
# roAssetRealizerEvent

event object returned roassetrealizerrealize method yield information success failure realization process

## ifAssetRealizerEvent

##### GetEvent() As Integer 

return integer value indicating type event



eventrealizesuccess specified sync list successfully realized
eventrealizeincomplete realization could begin least required file available pool
eventrealizefailedsafe realization failed nothing written destination likely safe continue realization process information failure available getfailurereason getname method
eventrealizefailedunsafe realization failed running change made destination file safe continue realization process information failure available getfailurereason getname method

##### GetName() As String

retrieves name affected file realization process fails

##### GetResponseCode() As Integer

retrieves rourltransfer response code associated event

##### GetFailureReason() As String

return additional information realization process fails

##### GetFileIndex() As Integer

retrieves zerobased index number file sync spec

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsrosyncspecmd
# roSyncSpec

object represents parsed sync spec allows retrieve various part specification method

## ifSyncSpec

##### GetFailureReason() As String

return information rosyncspec method indicates failure

##### ReadFromFile(filename As String) As Boolean

populates sync spec reading specified file method return true upon success false upon failure

##### ReadFromString(spec As String) As Boolean

populates sync spec reading passed string method return true upon success false upon failure

##### WriteToFile(filename As String) As Boolean

writes current sync spec specified file regenerated possible file textually identical specification read method return true upon success false upon failure

##### WriteToFile(filename As String, options As roAssociativeArray) As Boolean

writes current sync spec specified file json option associative array currently contain format parameter value json xmljson regenerated possible file textually identical specification read method return true upon success false upon failure

##### WriteToString() As String

writes current sync spec string return method return empty string write operation fails

##### WriteToString(options As roAssociativeArray) As String

writes current sync spec string return json option associative array currently contain format parameter value json method return empty string write operation fails

##### GetMetadata(section As String) As roAssociativeArray

return roassociativearray object containing information stored specified metadata section sync spec typically client server method return read operation fails

sync spec formatted returned value string spec spec formatted json javascript type converted follows

javascript type brightscript type

array roarray
object roassociativearray
string string
boolean boolean
number double
null invalid

##### LookupMetadata(section As String, field As String) As String

provides shortcut looking specified metadata item specified section without needing create temporary roassociativearray object method return empty string read operation fails

##### GetFileList(section As String) As roList

return rolist object containing roassociativearray object file specified section sync spec method return invalid read operation fails

##### GetFile(section As String, index As Integer) As roAssociativeArray

return roassociativearray object file specified section specified index method return invalid read operation fails

##### GetName() As String

return name supplied sync spec sync element

##### EqualTo(other As roSyncSpec) As Boolean

compare content rosyncspec object another rosyncspec object method compare parsed content sync spec rather file

##### VerifySignature(signature as String, obfuscated\_passphrase as String) As Boolean

deobfuscates passphrase us verify signature sync spec method return true upon success false upon failure

##### FilterFiles(section As String, criteria As roAssociativeArray) As roSyncSpec

return rosyncspec object copy existing object except specified section filtered using specified criterion criterion matched file metadata multiple criterion specified passed associative array criterion must file returned rosyncspec

following call yield rosyncspec object download section filtered file group script remain


filteredspec specfilterfilesdownload group script


##### FilesEqualTo(spec As roSyncSpec) As Boolean

compare content sync spec another sync spec return true theyre identical method compare parsed content sync spec rather xmljson

##### GetAssets(section As String) As Object

retrieves list asset sync spec form thats compatible roassetpool associated object

developersdevelopersbrightscriptobjectreferencecontentmanagementobjectsmd
# Content Management Objects



version older version

version

version

version

version

version

version

previous version


section describes object enable downloading storage retrieval content remote

roassetcollectioncontentmanagementobjectsroassetcollectionmd
roassetfetchercontentmanagementobjectsroassetfetchermd
roassetfetchereventcontentmanagementobjectsroassetfetchereventmd
roassetfetcherprogresseventcontentmanagementobjectsroassetfetcherprogresseventmd
roassetpoolcontentmanagementobjectsroassetpoolmd
roassetpoolfilescontentmanagementobjectsroassetpoolfilesmd
roassetrealizercontentmanagementobjectsroassetrealizermd
roassetrealizereventcontentmanagementobjectsroassetrealizereventmd
rosyncspeccontentmanagementobjectsrosyncspecmd

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsrodatetimemd
# roDateTime



version older version

version

version

version

version

version

version

previous version


object used represent instant time time creation object represents zero second javascript equivalent date

## ifDateTime

##### GetDayOfWeek() As Integer  


##### GetDay() As Integer  


##### GetMonth() As Integer  


##### GetYear() As Integer  


##### GetHour() As Integer  


##### GetMinute() As Integer  


##### GetSecond() As Integer  


##### GetMillisecond() As Integer  


##### SetDay(day As Integer) As Void  


##### SetMonth(month As Integer) As Void  


##### SetYear(year As Integer) As Void  


##### SetHour(hour As Integer) As Void  


##### SetMinute(minute As Integer) As Void  


##### SetSecond(second As Integer) As Void  


##### SetMillisecond(millisecond As Integer) As Void  


##### AddSeconds(seconds As Integer) As Void  


##### SubtractSeconds(seconds As Integer) As Void  


##### AddMilliseconds(milliseconds As Integer) As Void  


##### SubtractMilliseconds(milliseconds As Integer) As Void  


##### Normalize() As Boolean

check field supplied correct function fails value bound

##### ToIsoString() As String

return current rodatetime value iso8601 basic formatted string hyphen date colon time omitted comma used separate second millisecond example iso8601 standard 20140529t123000100 would formatted 20140529t123000100

method return empty string year less 1970 greater 2100 since unconfigured rodatetime object lie outside acceptable range also return empty string

##### FromIsoString(date-time As String) As Boolean

set value rodatetime object using iso8601 basic formatted string hyphen date colon time omitted either period comma used separate second millisecond iso8601 standard 20140529t123000100 could example formatted either 20140529t123000100 20140529t123000100 method return false indicating affected change rodatetime object string formatted incorrectly date passed outside range january 1970 december 2100

##### ToSecondsSinceEpoch() As Integer

return number second elapsed since midnight january 1970 represented rodatetime instance system time

##### FromSecondsSinceEpoch(seconds As Integer) As Boolean

populates rodatetime instance specified number second since midnight january 1970

##### GetString() As String

## ifString

##### GetString() As String

return current date using sortable date format yyyymmdd hhmmsssss

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsronetworktimeeventmd
# roNetworkTimeEvent



version older version

version

version

version

version

version

version

previous version


event object generated rosystemtime object

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifNetworkTimeEvent

##### WasSuccessful() As Boolean

return true last attempt clock network http successful

##### GetFailureReason() As String

return description error last attempt clock network failed

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsrosystemtimemd
# roSystemTime



version older version

version

version

version

version

version

version

previous version


object provides ability read write time stored realtime clock also used read write timezone setting javascript equivalent systemtime

note
date january 2038 supported

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type ronetworktimeevent attached message port

## ifSystemTime

##### GetLocalDateTime() As roDateTime

return current time modulated using current time zone rodatetime instance

##### GetUtcDateTime() As roDateTime

return current time modulated using utcgmt time zone rodatetime instance

##### GetZoneDateTime(timezone\_name As String) As Object

return current time modulated using specified time zone rodatetime instance supported time zone listed

##### SetLocalDateTime(local\_DateTime As roDateTime) As Boolean

specifies time using current time zone

##### SetUtcDateTime(utc\_DateTime As roDateTime) As Boolean

specifies time using utcgmt time zone

##### GetTimeZone() As String

return current timezone setting player posix value appended beginning string time zone using posix format

##### SetTimeZone(zone\_name As String) As Boolean

specifies timezone setting player supported time zone listed alternatively posix formatted time zone applied appending posix value beginning string

following code specifies posixformatted time zone


createobjectrosystemtime
tsettimezoneposixgmt0bst1m350100m1050200


##### IsValid() As Boolean

return true system time valid value time

##### GetLastNetworkTimeResult() As roAssociativeArray

return associative array containing information last attempt time network

successtimestamp value indicating clock last successfully network value zero clock never successfully network

attempttimestamp value indicating last attempt made clock network value zero attempt made

failurereason last attempt clock network failed string contain error message last attempt successful string empty


associative array timestamp refers number second since player booted value compared total uptime player retrieved calling uptime0

## Supported Time Zones 

following supported system time zone list apply posixformatted time zone

eastern time

central time

mountain time

pacific time

akst alaska time

hawaiialeutian time daylight saving hawaii

hst1 hawaiialeutian time daylight saving

mst1 without daylight saving time arizona

est1 without daylight saving time east indiana

atlantic time

cst2 mexico mexico city

mst2 mexico chihuahua

pst2 mexico tijuana

brazil time paulo

newfoundland time

azot azores time

gmtbst londondublin time

western european time

central european time

eastern european time

moscow time

samt delta time zone samara

yekt echo time zone yekaterinburg

indian standard time

nepal time

omst foxtrot time zone omsk

japanese standard time

christmas island time australia

awst australian western time

awst1 australian western time without daylight saving time

acst australian central standard time daylight saving time

acst1 darwin australiadarwin australian central standard time without daylight saving time

aest australian eastern time daylight saving time

aest1 australian eastern time without daylight saving time brisbane

norfolk island time australia

nzst zealand time auckland

chast fiji time fiji pacificfiji yankee time zone fiji

xray time zone pago pago

greenwich mean time

gmt1 hour behind greenwich mean time

gmt2 hour behind greenwich mean time

gmt3 hour behind greenwich mean time

gmt330 hour behind greenwich mean time

gmt4 hour behind greenwich mean time

gmt430 hour behind greenwich mean time

gmt5 hour behind greenwich mean time

gmt6 hour behind greenwich mean time

gmt7 hour behind greenwich mean time

gmt8 hour behind greenwich mean time

gmt9 hour behind greenwich mean time

gmt930 hour behind greenwich mean time

gmt10 hour behind greenwich mean time

gmt11 hour behind greenwich mean time

gmt12 hour behind greenwich mean time

gmt13 hour behind greenwich mean time

gmt14 hour behind greenwich mean time

gmt1 hour ahead greenwich mean time

gmt2 hour ahead greenwich mean time

gmt3 hour ahead greenwich mean time

gmt330 hour ahead greenwich mean time

gmt4 hour ahead greenwich mean time

gmt430 hour ahead greenwich mean time

gmt5 hour ahead greenwich mean time

gmt530 hour ahead greenwich mean time

gmt6 hour ahead greenwich mean time

gmt630 hour ahead greenwich mean time

gmt7 hour ahead greenwich mean time

gmt730 hour ahead greenwich mean time

gmt8 hour ahead greenwich mean time

gmt830 hour ahead greenwich mean time

gmt9 hour ahead greenwich mean time

gmt930 hour ahead greenwich mean time

gmt10 hour ahead greenwich mean time

gmt1030 hour ahead greenwich mean time

gmt11 hour ahead greenwich mean time

gmt1130 hour ahead greenwich mean time

gmt12 hour ahead greenwich mean time

gmt1230 hour ahead greenwich mean time

gmt13 hour ahead greenwich mean time

gmt14 hour ahead greenwich mean time

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsrotimermd
# roTimer



version older version

version

version

version

version

version

version

previous version


object allows script trigger event specific datetime specified interval event triggered delivering rotimerevent object specified message port javascript equivalent settimeoutsetinterval

## ifTimer

##### SetTime(hour As Integer, minute As Integer, second As Integer, millisecond As Integer) As Void

set time event trigger general value wildcard cause event trigger every time rest specification match wildcards timer trigger specified time occurs

note
periodic timer fire every second supported second millisecond parameter must zero wildcards elsewhere

##### SetTime(a As Integer, b As Integer, c As Integer)  


##### SetDate(year As Integer, month As Integer, day As Integer) As Void

set date event trigger general value wildcard cause event trigger every time rest specification match wildcards timer trigger specified datetime occurs

##### SetDayOfWeek(day\_of\_week As Integer) As Void

set week event trigger general value wildcard cause event trigger every time rest specification match wildcards timer trigger specified datetime occurs

note
possible using combination setdate setdayofweek call specify invalid combination never occur specification include wildcard second millisecond specification must zero event raised minute near whole minute

##### SetDateTime(date\_time As roDateTime) As Void

set time wish event trigger rodatetime object possible wildcards using method

##### Start() As Boolean

start timer based current value specified using function

##### Stop() As Void

stop timer

##### SetElapsed(seconds As Integer, milliseconds As Integer)

configures timer trigger specified time period elapsed unlike absolute timer method change system clock affect period setelapsed timer

## ifMessagePort

##### SetPort(port As roMessagePort) As Void

post message type rotimerevent attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifIdentity

##### GetIdentity() As Integer

return unique number used identify event originate object

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## Examples

script us setelapsed method create timer trigger every second


main
createobjectromessageport
timer createobjectrotimer
timersetportmp

timersetelapsed30

print start uptime0
timerstart

true
mpwaitmessage0
typeev rotimerevent
print timer event received uptime0
timerstart
else
print another event arrived typeev





script creates timer trigger every minute using wildcards timer spec


stcreateobjectrosystemtime
timercreateobjectrotimer
mpcreateobjectromessageport
timersetportmp

timersetdate1
timersettime1
timerstart

true
wait0
typeev rotimerevent
print timer event received
else
print unexpected event received
endif
endwhile


script creates timer trigger specific datetime


timercreateobjectrotimer
mpcreateobjectromessageport
timersetportmp

timersetdate2008
timersettime0

timerstart

true
wait0
typeev rotimerevent
print timer event received
else
print unexpected event received
endif
endwhile


developersdevelopersbrightscriptobjectreferencedateandtimeobjectsrotimereventmd
# roTimerEvent



version older version

version

version

version

version

version

version

previous version


event object generated rotimer object

## ifUserData

##### SetUserData(user\_data As Object)

set user data

##### GetUserData() As Object

return user data previously setuserdata either source event object return invalid data

## ifSourceIdentity

##### GetSourceIdentity() As Integer

retrieves identity value used associate event source rotimer instance

note
ifsourceidentity interface deprecated recommend using ifuserdata interface instead

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsrotimespanmd
# roTimeSpan



version older version

version

version

version

version

version

version

previous version


object provides interface simple timer tracking duration activity useful tracking long action taken whether specified time elapsed starting event javascript equivalent date

## ifTimeSpan

##### Mark()  


##### TotalMilliseconds() As Integer  


##### TotalSeconds() As Integer  


##### GetSecondsToISO8601Date(a As String) As Integer

#####

developersdevelopersbrightscriptobjectreferencedateandtimeobjectsmd
# Date and Time Objects



version older version

version

version

version

version

version

version

previous version


section describes object manipulate date time setting player

rodatetimedateandtimeobjectsrodatetimemd
ronetworktimeeventdateandtimeobjectsronetworktimeeventmd
rosystemtimedateandtimeobjectsrosystemtimemd
rotimerdateandtimeobjectsrotimermd
rotimereventdateandtimeobjectsrotimereventmd
rotimespandateandtimeobjectsrotimespanmd

developersdevelopersbrightscriptobjectreferencefileobjectsroappendfilemd
# roAppendFile

object used create file append information existing file

object creation creating roappendfile object open existing file creates file current position file writes made file


createobjectroappendfile filename string


## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

set sequence writing stream default value crlf need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### SendByte(byte As Integer) As Void

writes specified byte stream

##### SendLine(string As String) As Void

writes specified character stream followed current sequence

##### SendBlock(a As Dynamic) As Void

writes specified character stream method support either string robytearray block string null byte terminate block

##### Flush() As Void

writes stream file blocking execution data written

##### AsyncFlush() As Void

writes stream file within second system block execution writing file

note
system performs asynchronous flush automatically object instance destroyed instance variable containing reassigned stream first written kernel writes file system resource available

## ifStreamPosition

##### CurrentPosition() As Integer

return current position within file

developersdevelopersbrightscriptobjectreferencefileobjectsrocreatefilemd
# roCreateFile

object used write file overwrite existing file

object creation creating rocreatefile object open existing file creates file file exists truncated size zero


createobjectrocreatefile filename string


## ifReadStream

##### SetReceiveEol(eol\_sequence As String) As Void

set sequence reading stream

##### ReadByte() As Integer

read single byte stream blocking necessary reached error condition value less returned

##### ReadByteIfAvailable() As Integer

read single byte stream available byte available return immediately return value less indicates either reached byte available

##### ReadLine() As String

read find complete line sequence fails find sequence within 4096 byte return 4096 byte found data discarded case

##### ReadBlock(size As Integer) As String

read specified number byte number limited 65536 byte event error fewer byte requested returned null byte file mask byte

##### AtEof() As Boolean

return true attempt made read beyond file current position file attempt made read beyond method return false

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

set sequence writing stream default value crlf need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### SendByte(byte As Integer) As Void

writes specified byte stream

##### SendLine(string As String) As Void

writes specified character stream followed current sequence

##### SendBlock(a As Dynamic) As Void

writes specified character stream method support either string robytearray block string null byte terminate block

##### Flush() As Void

writes stream file blocking execution data written

##### AsyncFlush() As Void

writes stream file within second system block execution writing file

note
system performs asynchronous flush automatically object instance destroyed instance variable containing reassigned stream first written kernel writes file system resource available

## ifStreamSeek

##### SeekAbsolute(offset As Integer) As Void

seek specified offset offset beyond file file extended upon next write previously unoccupied space filled null byte

##### SeekRelative(offset As Integer) As Void

seek specified offset relative current position ultimate offset beyond file file extended described seekabsolute

##### SeekToEnd() As Void

seek file

##### CurrentPosition() As Integer

retrieves current position within file

developersdevelopersbrightscriptobjectreferencefileobjectsroreadfilemd
# roReadFile

object creation creating roreadfile object open specified file reading object creation fails file exist


createobjectroreadfile filename string


## ifStreamRead

##### SetReceiveEol(eol\_sequence As String) As Void

set sequence reading stream default character ascii value need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### ReadByte() As Integer

read single byte stream blocking necessary reached error condition value less returned

##### ReadByteIfAvailable() As Integer

read single byte stream available byte available return immediately return value less indicates either reached byte available

##### ReadLine() As String

read find complete line sequence fails find sequence within 4096 byte return 4096 byte found data discarded case

##### ReadBlock(size As Integer) As String

read specified number byte number limited 65536 byte event error fewer byte requested returned null byte file mask byte

##### AtEof() As Boolean

return true attempt made read beyond file current position file attempt made read beyond method return false

## ifStreamSeek

##### SeekAbsolute(offset As Integer) As Void

seek specified offset offset beyond file file extended upon next write previously unoccupied space filled null byte

##### SeekRelative(offset As Integer) As Void

seek specified offset relative current position ultimate offset beyond file file extended described seekabsolute

##### SeekToEnd() As Void

seek file

##### CurrentPosition() As Integer

retrieves current position within file

developersdevelopersbrightscriptobjectreferencefileobjectsroreadwritefilemd
# roReadWriteFile

object open file allows reading writing operation file

object creation creating roreadwritefile object open existing file reading writing object creation fails file exist current position beginning file


createobjectroreadwritefile filename string


## ifReadStream

##### SetReceiveEol(eol\_sequence As String) As Void

set sequence reading stream

##### ReadByte() As Integer

read single byte stream blocking necessary reached error condition value less returned

##### ReadByteIfAvailable() As Integer

read single byte stream available byte available return immediately return value less indicates either reached byte available

##### ReadLine() As String

read find complete line sequence fails find sequence within 4096 byte return 4096 byte found data discarded case

##### ReadBlock(size As Integer) As String

read specified number byte number limited 65536 byte event error fewer byte requested returned null byte file mask byte

##### AtEof() As Boolean

return true attempt made read beyond file current position file attempt made read beyond method return false

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

set sequence writing stream default value crlf need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### SendByte(byte As Integer) As Void

writes specified byte stream

##### SendLine(string As String) As Void

writes specified character stream followed current sequence

##### SendBlock(a As Dynamic) As Void

writes specified character stream method support either string robytearray block string null byte terminate block

##### Flush() As Void

writes stream file blocking execution data written

##### AsyncFlush() As Void

writes stream file within second system block execution writing file

note
system performs asynchronous flush automatically object instance destroyed instance variable containing reassigned stream first written kernel writes file system resource available

## ifStreamSeek

##### SeekAbsolute(offset As Integer) As Void

seek specified offset offset beyond file file extended upon next write previously unoccupied space filled null byte

##### SeekRelative(offset As Integer) As Void

seek specified offset relative current position ultimate offset beyond file file extended described seekabsolute

##### SeekToEnd() As Void

seek file

##### CurrentPosition() As Integer

retrieves current position within file



developersdevelopersbrightscriptobjectreferencefileobjectsmd
# File Objects



version older version

version

version

version

version

version

version

previous version


section describes object creating deleting manipulating file javascript equivalent file

manipulating file system require create object find documentation creating deleting directory file along file system manipulation function pageobjectreferenceglobalfunctionsmd

roappendfilefileobjectsroappendfilemd
rocreatefilefileobjectsrocreatefilemd
roreadfilefileobjectsroreadfilemd
roreadwritefilefileobjectsroreadwritefilemd

developersdevelopersbrightscriptobjectreferenceglobalfunctionsmd
# Global Functions

brightscript provides standard modulescope function stored global object global function referenced compiler directs runtime call appropriate global object member calling global function need operatorbrightscriptlanguagereferenceoperatorsmd reference roglobal object

note
global trigonometric function accept return value radian degree

## ifGlobal

##### CreateObject(name As String) As Object

creates brightscript object corresponding specified class name method return invalid object creation fails object parameter constructor must passed class name commaseparated list


createobjectrogpiocontrolport
serial createobjectroserialport 9600


##### RestartScript() As Void

exit current script system scan valid autorunbrs file

##### RestartApplication() As Void

restarts brightsign application

##### Sleep(milliseconds As Integer)

instructs script pause specified amount time without wasting cycle sleep interval specified millisecond

##### asc(letter As String) As Integer

return ascii code first character specified string nullstring argument cause error

##### chr(character As Integer) As String

return onecharacter string containing character reflected specified ascii control example quotation mark normally used string delimiters pas ascii code function quote string

##### len(target\_string As String) As Integer

return number character string

##### str(value As Double) As String

convert specified float value string method also return string equal character representation value example assigned value calling stra return string

##### strI(value As Integer) As String

convert specified integer value string method return string equal character representation value always leading space nonnegative number example assigned value calling stria return string

rointrofloatrostringtostrasstring need alternate method return string without prepended space

##### val(target\_string As String) As Double

return number represented character string argument opposite function example assigned string assigned string calling valab return float value

##### strtoi(target\_string As String) As Integer

convert target string integer noninteger character including decimal point space number right noninteger character part integer output

##### abs(x As Double) As Double

return absolute value argument

##### atn(x As Double) As Double

return arctangent radian argument atnx return angle whose tangent arctangent degree multiply atnx 5729578

##### csng(x As Integer) As Float

return singleprecision float representation argument

##### cdbl(x As Integer) As Double

return doubleprecision float representation argument

##### cint(x As Double) As Integer

return integer representation argument rounding nearest whole number

##### cos(x As Double) As Double

return cosine arugment argument must radian obtain cosine degree cosx01745329

##### exp(x As Double) As Double

return natural exponential inverse function

##### fix(x As Double) As Integer

return truncated representation argument digit right decimal point removed resultant value integer nonnegative value fixx equal intx negative value fixx equal intx1

##### int(x As Double) As Integer

return integer representation argument using largest whole number greater argument example int22 return int25 return

##### log(x As Double) As Double

return natural logarithm argument logex inverse function find logarithm number base following formula logbx logexlogeb

##### sgn(x As Double) As Integer

return integer representing float argument signed negative zero positive

##### sgnI(x As Integer) As Integer

return integer representing integer argument signed negative zero positive

##### sin(x As Double) As Double

return sine argument argument must radian obtain sine degree sinx01745329

##### tan(x As Double) As Double

return tangent argument argument must radian obtain tangent degree tanx01745329

##### sqr(x As Double) As Double

return square root argument function calculates result faster

##### StableEnumeration(array as Object) As Object

return object represents iteration function affect original object must function safely enumerate container parallel

##### Left(target\_string As String, n As Integer) As String

return first character specified string

##### Right(target\_string As String, n As Integer) As String

return last character specified string

##### StringI(n As Integer, character As Integer) As String

return string composed character symbol repeated time character symbol passed method ascii code integer

##### String(n As Integer, character As String) As String

return string composed character symbol repeated time character symbol passed method string

##### Mid(target\_string As String, start\_position As Integer, length As Integer) As String

return substring target string first integer passed method specifies starting position substring second integer specifies length substring start position string begin

##### Instr(start\_position As Integer, search\_text As String, substring As String) As Integer 

return position substring within string function case sensitive return specified substring found start position string begin



string object also offer instr method though us zerobased index rostringobjectreferencebrightscriptcoreobjectsrointrofloatrostringmd documentation detail

##### FindMemberFunction(object as Object, funName as String) As Interface

return interface object provides specified function else return invalid available rodeviceinfohasfeaturefindmemberfunction return true

used shown


print findmemberfunction count interface ifassociativearray


##### GetInterface(object As Object, ifname As String) As Interface

return value type interface object interface case skip interface specification calling object component cause problem long method name within function unique

##### Wait(timeout As Integer, port As Object) As Object

instructs script wait object ifmessageport interface method return event object posted message port timeout specified zero wait wait indefinitely otherwise wait return invalid specified number millisecond message received


createobjectromessageport
createobjectrogpiocontrolport
swsetportp
msgwait0
print typemsg rogpiobutton
print msggetint button number


##### ReadAsciiFile(file\_path As String) As String

read specified text file return string

##### WriteAsciiFile(file\_path As String, buffer As String) As Boolean

creates text file specified file path text file passed second parameter method cannot used edit file preexisting text file overwritten name directory path created

note
rocreatefileobjectreferencefileobjectsrocreatefilemd object provides flexibility need create edit file

##### ListDir(path As String) As Object

return rolistobjectreferencebrightscriptcoreobjectsrolistmd object containing content specified directory path file name converted lowercase

##### MatchFiles(path As String, pattern\_in As String) As Object

take directory look simple pattern matched return rolistobjectreferencebrightscriptcoreobjectsrolistmd containing result listed result contains part filename matched pattern full path match applied specified directory result pattern contains directory separator pattern case insensitive wildcard expression contain following special character

match single character

match zero arbitrary character

match single character specified within bracket closing bracket treated member character class immediately follows opening bracket match single closed bracket within class used specify range unless first last character acfh equivalent abcfgh character class negated specifying first character match literal character place elsewhere class


note
special character lose function preceded single single matched using

##### LCase(target\_string As String) As String

convert specified string lowercase

##### UCase(target\_string As String) As String

convert specified string uppercase

##### DeleteFile(file\_path As String) As Boolean

deletes file specified file path method return false delete operation fails file exist

##### DeleteDirectory(directory As String) As Boolean

deletes specified directory method recursively delete file directory necessary removing specified directory method return false fails delete directory still delete nested file directory

example


deletedirectorydirectory
check directory deletion successful
print true successful





deletedirectorydirectory

print could delete directory



##### CreateDirectory(directory As String) As Boolean

creates specified directory directory created time method return true upon success false upon failure

example


createdirectorydirectory
check directory creation successful
print true successful





createdirectorydirectory

print could create directory



##### RebootSystem() As Void

instructs player perform soft reboot

##### ShutdownSystem() As Void  


##### UpTime(dummy As Integer) As Double

return uptime system second since last reboot

##### FormatDrive(drive As String, fs\_type As String) As Boolean 

format specified drive using file system listed function return true upon success false upon failure

vfat fat32 doswindows file system readable writable window linux macos

exfat doswindows file system supported series xtx43 xdx33 hdx23 ls423 ho523 series xtx44 xdx34 hdx24 ls424 player firmware version 6294 later secure boot supported exfat filesystem firmware version 6294

ext2 linux file system writable linux readable window macos additional software

ext3 linux file system writable linux readable window macos additional software

ext4 linux file system writable linux readable window macos additional software recommended file system device hard drive


##### EjectDrive(drive As String) As Boolean

ejects specified drive return true successful script currently accessing file specified drive ejection process fail

##### CopyFile(source As String, destination As String) As Boolean

copy file specified source filepath specified destination directory function return true successful false event failure

##### MoveFile(source As String, destination As String) As Boolean

move specified source file specified destination directory function return true successful false event failure

note
path name must drive

##### MapFilenameToNative(path As String) As String

convert specified brightscriptstyle path corresponding native path return string path sdmydir returned storagesdmydir

##### rnd(a As Dynamic) As Dynamic

##### RunGarbageCollector() As roAssociativeArray

destroys object currently state circular reference counting brightscript normally remove object become unreferenced part automated garbage collection algorithm however object reference never reach reference count zero need destroyed manually using method

method useful destroying presentation data structure generating presentation method return associative array outlining result garbagecollection process

##### GetDefaultDrive() As String

return current default drive complete trailing slash running autorunbrs drive containing autorun designated current default

##### SetDefaultDrive(drive As String)

set current default drive need include trailing slash method fail however specified default drive exist possible retrieve anything

method accepts following value

usb1 drive storage device connected player

primary microsd drive player

internal microsd drive player 4kx42 xdx32 model

internal player xtx44 xtx34 xdx34 xdx33 model


##### EnableZoneSupport(enable As Boolean)

allows display multiple video html image text zone firmware zone support enabled default

##### EnableAudioMixer(enable As Boolean)

##### Pi() As Double

return value doubleprecision floatingpoint number

##### ParseJson(json\_string As String) As Object

parses string formatted according rfc4627 standard return equivalent brightscript object consist following booleans integer floating point number string roarray object roassociativearray object parsejson method following property

invalid returned string syntactically correct

roassociativearray object returned case sensitive

error returned roarray roassociativearray nested level deep


following script demonstrates parsejson process json object containing title url image

##### JSON Script



photo

title view hotel



title relaxing beach



title flat tire






##### BrightScript


searchrequest createobjectrourltransfer
searchrequestseturl
response parsejsonsearchrequestgettostring
photo responsephotos
getimagephototitle photourl



##### FormatJson(json As roAssociativeArray, flags As Integer) As String

convert associative array json string formatted according rfc4627 standard following supported data type boolean integer float string roarray roassociativearray flag parameter specified nonascii character escaped output string uxxxx xxxx hexadecimal representation unicode character value flag parameter nonascii character escaped

array associative array nested level deep error occur error occurs empty string returned

caution
important
default using objectliteral syntax aarelativepathfoo generate associative array convert key lower case preserve camel case json roassociativearrayaddreplace method instead object literal call roassociativearraysetmodecasesensitive adding entry

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsroblockciphermd
# roBlockCipher

object provides mean symmetric block encryption currently support cipher block size bit javascript equivalent nodejs crypto

object creation roblockcipher object created associative array representing parameter


createobjectroblockcipher parameter roassociativearray


associative array contain following parameter

mode aes128cbc aes192cbc aes256cbc

padding zero pkcs7 object default zero padding parameter omitted


padding required input exact multiple cipher block size specifying zero padding needed specifying pkcs7 always add padding even data already multiple block size case entire block added pkcs7 padding automatically removed upon decryption zero padding retained since mean unambiguously distinguish value data

## ifBlockCipher

##### SetIV(iv As Object) As Void

set initialization vector cipherblockchaining mode supplied shorter required zero padded passing empty string vector zero typically contain arbitrary character form robytearray though also string

##### Encrypt(key As Object, plaintext As Object) As roByteArray

us specified encrypt plaintext parameter passed either string robytearray

##### Decrypt(key As Object, cipher\_text As Object) As roByteArray

us specified decrypt cipher text passed robytearray cipher text encrypted contain character

##### **Example**


case4 rfc3602
createobjectrobytearray
createobjectrobytearray
plain createobjectrobytearray
keyfromhexstring56e47a38c5598974bc46903dba290349
ivfromhexstring8ce82eefbea0da3c44699ed7db51b7d9 plainfromhexstringa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedf
createobjectroblockcipher mode aes128cbc
csetiviv
crypt cencryptkey plain
result crypttohexstring
expected ucasec30e32ffedc0774e6aff6af0869f71aa0f3af07a9a31a9c684db207eb0ef8e4e35907aa632c3ffdf868bb7b29d3d46ad83ce9f9a102ee99d49a53e87f4c3da55


decrypt example recover encrypted data
csetiviv
roundtrip cdecryptkey crypt


second example selecting pkcs7 padding
createobjectroblockcipher mode aes128cbc padding pkcs7


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrobrightpackagemd
# roBrightPackage

robrightpackage object represents file include arbitrary content installed storage device provide content script update example distribute update thumb drive javascript equivalent nodejs zlib

object creation robrightpackage object created filename parameter specifies name file


createobjectrobrightpackage filename string


limitation

robrightpackage object support file smaller

supported technology

deflate32 default option

ppmd default option

winzip compression maximum superfast option option including enhanced deflate supported

encryption


unsupported technology

bzip2

lzma

deflate64

zip64 compression software built window explorer


## ifBrightPackage

note
ifbrightpackage legacy interface recommend roassetpool instead achieve better functionality

##### Unpack(path As String) As Void

extract file specified destination path preexisting file target directory deleted part operation providing destination path wipe preexisting file card extract content root folder

##### SetPassword(password As String) As Void

provides password specified file created method support encryption generated winzip

##### GetFailureReason() As String  


##### UnpackFile(a As String, b As String) As Boolean

##### **Example**


package createobjectrobrightpackage newfileszip
packagesetpasswordtest
packageunpacksd


## Using roBrightPackage for Content Updates

brightsign player check storage device autorun script following order

external device






addition looking autorunbrs script brightsign player look autorunzip file contain script name autozipbrs autorunzip file autozipbrs file found autozipbrs decrypted player execute autozipbrs file

caution
important
autozipbrs file cannot reference external file file automatically uncompressed brightsign player prior execution

autozipbrs script unpack content autorunzip file installed storage device reboot complete update

##### **Example**


package createobjectrobrightpackage sdautorunzip
packageunpacksd
movefilesdautorunzip sdautorunzipinvalid
rebootsystem


### Unpacking Encrypted Archives

autorunzip file encrypted player us password stored registryhashingandstorageobjectsroregistrymd section security name autozipkey decrypt file

##### **Extended Example**


content update application


rcreateobjectrorectangle 1240
tcreateobjectrotextwidgetr121
rcreateobjectrorectangle 1200
tsetsafetextregionr
tsetforegroundcolorhff303030
tsetbackgroundcolorhffffffff
tpushstringupdating content drive please wait


package createobjectrobrightpackage autorunzip
packagesetpasswordtest
packageunpacksd
package


tclear
tpushstringupdate complete remove drive restart


true
sleep1000


usbkey createobjectroreadfile usb1autorunzip
typeusbkey roreadfile
arebootsystem
endif
usbkey



developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrodiskerroreventmd
# roDiskErrorEvent

object returned waiting message port connected rodiskmonitor object

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifDiskErrorEvent

##### GetDiskError() As Object

return roassociativearray containing following parameter



type description
source rostring error type
time rodatetime time error occurred millisecond accuracy
device rostring internal name device generating error
error rostring description error egtimeout
param rostring error parameter depends type error sector number

example


msgpgetdiskerror
report time aatime error aasource aaerror aadevice aaparam


note
example us implicit conversion rodatetime could also rodatetimegetstring

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrodiskmonitormd
# roDiskMonitor

object provides access lowlevel information disk error provides eventbased interface delivers rodiskerrorevent object romessageport error message held five second delivery minimize chance spurious error report error reported disk removed five second interval diskremoval detection take several second allows longterm monitoring occasional medium error

object creation rodiskmonitor object created parameter


createobjectrodiskmonitor


## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rodiskerrorevent attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

##### **Example**


diskmoncreateobjectrodiskmonitor

msgpcreateobjectromessageport
diskmonsetportmsgp


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrohashgeneratormd
# roHashGenerator

object allows generate variety message digest javascript equivalent nodejs crypto

object creation hashing algorithm specified creating rohashgenerator object


createobjectrohashgenerator algorithm string


algorithm parameter accepts following string

sha256

sha384

sha512

sha1



crc32


note
crc32 available firmware version later

## ifHashGenerator

##### Hash(obj As Object) As Object

hash payload supplied form string object implementing ifstring robytearray hash returned robytearray

##### SetHmacKey(key As Dynamic) As Boolean

supply cryptographic hashing function method accepts plaintext

##### SetObfuscatedHmacKey(key As String) As Boolean

supply cryptographic hashing function method accepts obfuscated using shared secret

##### GetFailureReason() As String

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsropasskeymd
# roPassKey

object provides mean generating key hash password salt javascript equivalent nodejs crypto

object creation object passed associative array specifies generation method cipher


createobjectropasskey parameter roassociativearray


associative array contain following parameter

method derivation method currently pbkdf2 specified

keyfn pseudorandom function currently hmacsha256 specified

keylen length

iteration number iteration


## ifPassKey

##### GenerateKey(password As Object, salt As Object) As roByteArray

generates using supplied password salt parameter passed either string robytearray instance generated robytearray instance contain possible byte value including

##### GenerateSalt(length As Integer) As roByteArray

generates salt specified length salt used calling generatekey method generated robytearray instance contain possible byte value including

##### **Example**


create input test data
salt createobjectrobytearray
pas createobjectrobytearray
passfromasciistringpassword
saltfromasciistringsalt
create generator
createobjectropasskey method pbkdf2 keyfn hmacsha256 keylen iteration 4096
robytearray
pkgeneratekeypass salt


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsroregistrymd
# roRegistry

registry area memory small number persistent setting stored access registry available roregistry object javascript equivalent registry brightscriptjavascript migration guidedevelopersplayerapisbrightscriptjavascriptmigrationguidemd method equivalent

object created parameter


createobjectroregistry


## ifRegistry

##### GetSectionList() As roList

return list entry registry section

##### Delete(section As String) As Boolean

deletes specified section return indication success

##### Flush() As Boolean

flush registry persistent storage

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsroregistrysectionmd
# roRegistrySection

object represents section registry enabling organization setting within registry allows section read written javascript equivalent registry brightscriptjavascript migration guidedevelopersplayerapisbrightscriptjavascriptmigrationguidemd method equivalent

object creation object must supplied registrysection name upon creation


createobjectroregistrysection section string


writes always take effect immediately prevent system exceeding maximum number writes onboard persistent storage second write registry newly written data automatically written persistent storage reason change must written immediately flush method called change written automatically prior exiting application

## ifRegistrySection

##### Read(key As String) As String

read return value specified performing read entry exist within section exist return empty string

##### Write(key As String, value As String) As Boolean

replaces value specified

##### Delete(key As String) As Boolean

deletes specified

##### Exists(key As String) As Boolean

return true specified exists

##### Flush() As Boolean

flush content registry persistent storage

##### GetKeyList() As roList

return list containing entry registry section

##### **Example**


registrysection createobjectroregistrysection widgetusage
empty entry read empty string therefore converted zero
hit valregistrysectionreadbigredbuttonhits
hit hit
registrysectionwritebigredbuttonhits strihits


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrosqlitedatabasemd
# roSqliteDatabase

main sqlite object owns database create many object need javascript equivalent indexeddb

## ifSqliteDatabse

##### Open(path As String) As Boolean

open existing database file method return true upon success

##### Create(path As String) As Boolean

creates empty database file method return true upon success

passing memory method creates database nonpersistent storage useful highvolume database application might cause wear issue card

##### Close()

close open database

##### CreateStatement(sql\_text As String) As Object

creates rosqlitestatement object using specified string

##### RunBackground(sql\_text As String, associative\_array As Object) As Integer

run specified statement background bind variable using passed roassociativearray

##### SetMemoryLimit(limit As Integer)

set soft memory limit sqlite attempt remain sqlite documentation detail

note
setmemorylimit method set global parameter must therefore called call made database object

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rosqliteevent attached message port

## Examples

creating database


createobjectrosqlitedatabase

print

openresult dbcreatesdtestdb

openresult
print created
else
print creation failed

endif


creating table database


createstmt dbcreatestatementcreate table playback text primary path path playbackcount

print createstmt

typecreatestmt rosqlitestatement
print didnt statement returned

endif

sqlresult createstmtrun

print sqlresult

sqlresult sqlitecomplete
print table created
else
print table creation failed
endif

createstmtfinalise


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrosqliteeventmd
# roSqliteEvent

event object returned runbackground operation called associated rosqlitedatabase object

## ifSqliteEvent

##### GetTransactionId() As Integer

return integer match result originating runbackground operation

##### GetSqlResult() As Integer

return result code returned rosqlitestatementrun method possible return value identical method

statement complete

busy

row available


note
method used asynchronous alternative method

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrosqlitestatementmd
# roSqliteStatement

object created calling createstatement method rosqlitedatabase object javascript equivalent indexeddb

## ifSqliteStatement

bind method return true upon success

##### BindByName(associative\_array As Object) As Boolean

bind variable using name contained statement

##### BindByOffset(associative\_array/enumerable As Object) As Boolean

bind variable using index contained statement passed associative array method convert key associative array numeric offset binding passed enumerable object roarray bind value enumerable order stored

##### BindText(variable/index As Object, value As String) As Boolean

bind variable indicated name index parameter passed string value

##### BindInteger(variable/index As Object, value As Integer) As Boolean

bind variable indicated name index parameter passed integer value

##### Run() As Integer

run statement immediately wait integer result following possible integer result code

statement complete

busy

row available


##### RunBackground() As Integer

run statement background rosqlitedatabasesetport message port receive rosqliteevent message later point runbackground call result integer transaction appear rosqliteevent message match transaction

##### GetData() As Object

return associative array namevalue pair available select similar operation

##### Finalise()

finalizes statement method applied statement parent database closed object used method called also note object automatically finalized deleted

## Examples

following script insert table using bindbyname method


insertstmt dbcreatestatementinsert playback md5pathplaybackcount valuesmd5parampathparampcparam

print insertstmt

typeinsertstmt rosqlitestatement
print didnt statement returned

endif

params md5param abdef12346 pathparam foobarbingbong pcparam

bindresult insertstmtbindbynameparams

bindresult
print bindbyname
else
print bindbyname failed

endif

sqlresult insertstmtrun

print sqlresult

sqlresult sqlitecomplete
print table insertion
else
print table insertion failed
endif

insertstmtfinalise


following script insert table background


example assume message port rosqlitedatabase instance


insertstmt dbcreatestatementinsert playback md5pathplaybackcount valuesmd5parampathparampcparam

print insertstmt

typeinsertstmt rosqlitestatement
print didnt statement returned

endif

params md5param abdef12348 pathparam foobarbingbong pcparam

bindresult insertstmtbindbynameparams

bindresult
print bindbyname
else
print bindbyname failed

endif

expectedid insertstmtrunbackground

mpwaitmessage10000
invalid
typee rosqliteevent
transid egettransactionid
sqlresult egetsqlresult
print transid
print sqlresult
transid expectedid
print incorrect transaction

endif
sqlresult sqlitecomplete
print insertion failed

endif
else
print runbackground wrong event failed

endif
else
print runbackground response failed

endif

dont need call finalise since thatll done background processor


following script query table


selectstmt dbcreatestatementselect playback

typeselectstmt rosqlitestatement
print didnt statement returned

endif

sqlresult selectstmtrun

print sqlresult

sqlresult sqliterows
resultsdata selectstmtgetdata
print resultsdata
sqlresult selectstmtrun


selectstmtfinalise


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrostorageattachedrostoragedetachedmd
# roStorageAttached, roStorageDetached

event object generated rostoragehotplug object whenever storage device becomes attached detached player javascript equivalent nodejs fswatch

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifString

##### GetString() As String  


##### SetString(a As String)

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrostoragehotplugmd
# roStorageHotplug

object provides rostorageattached message storage device appear rostoragedetached message storage device disappear rostorageattached event delivered filesystem mounted javascript equivalent nodejs fswatch

currently poll medium

object creation rostoragehotplug object created parameter


createobjectrostoragehotplug


## ifStorageHotplug

##### GetStorageStatus(drive As String) As roAssociativeArray

return current status storage device even mounted method return associative array containing following

value type description

present boolean indicates whether specified device present
mounted boolean indicates whether specified device mounted
corrupt boolean indicates whether specified device believed corrupt
checking boolean indicates whether specified device currently checked

note
result getstoragestatus method unreliable called usbn parameter positive integer indicating storage device multiple device connected player

example


status createobjectrostoragehotpluggetstoragestatusssd
statusmounted statuschecking statuspresent
confirmation
formatdrivessd



## ifFailureReason

##### GetFailureReason() As String

return additional diagnostic information method return false

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rostorageattached rostoragedetached attached message port

note
order avoid race condition startup check storage device might existed prior message port recommend object created message port instructing script wait event

## Example


main
createobjectromessageport
createobjectrostoragehotplug
gpio createobjectrocontrolport brightsign

shsetportmp
gpiosetportmp

finished false
finished
mpwaitmessage0
typeev rocontroldown
finished true
else typeev rostorageattached
print attached evgetstring
else typeev rostoragedetached
print detached evgetstring
else
print typeev
stop





developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrostorageinfomd
# roStorageInfo

object used report usage information storage device

object creation rostorageinfo object created parameter specifies path storage device path need extend root storage device javascript equivalent filesysteminfo storageinfo brightscriptjavascript migration guidedevelopersplayerapisbrightscriptjavascriptmigrationguidemd method equivalent


createobjectrostorageinfo path string


### Drive Specifications 

following string value specify different storage drive

usb1 drive storage device connected player

primary microsd drive player

internal microsd drive player 4kx42 xdx32 model

internal player xtx44 xtx43 xdx34 xdx33 model


## ifStorageInfo

##### GetFailureReason() As String

yield additional useful information function return indicates error

##### GetBytesPerBlock() As Integer

return size native block filesystem used specified storage device

##### GetSizeInMegabytes() As Integer

return total size mebibyte storage device

caution
important
filesystems portion space reserved super user following expression true getusedinmegabytes getfreeinmegabytes getsizeinmegabytes

##### GetUsedInMegabytes() As Integer

return amount mebibyte space currently used storage device amount includes size pool class integrate pool calculation

##### GetFreeInMegabytes() As Integer

return available space mebibyte storage device

##### GetFileSystemType() As String

return string describing type filesystem used specified storage whether encrypted ecryptfs following potential value

exfat

ext3

ext4

fat12

fat16

fat32



hfsplus

ntfs

ecryptfs version 901451


##### GetStorageCardInfo() As roAssociativeArray

return associative array containing detail storage device hardware card returned data include following



sdmfrid integer card manufacturer assigned card association
sdoemid string twocharacter card identifier assigned card association
sdproductname string product name assigned card manufacturer byte byte
sdspecvers integer version spec card conforms
sdproductrev string product revision assigned card manufacturer
sdspeedclass string speed class declared card
sdausize integer size byte

example


sicreateobjectrostorageinfo
print sigetfreeinmegabytes free


developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsrovirtualmemorymd
# roVirtualMemory

rovirtualmemory object allows create virtual memory repository chromium html engine allows chromium automatically swap unused element physical memory

object available platform support ssdmsata drive xtx44 xtx43 xdx34 xdx33 4kx42

object creation object instantiated without parameter


createobjectrovirtualmemory


## ifVirtualMemory

##### AddSwapFile(parameters As roAssociativeArray) As Boolean

add virtual memory repository local storage method accepts associative array following parameter

filename string swap file created possible specify file location ssdmsata drive recommended

megabyte size swap file created


specified file already exist created already exists size modified either operation take time need called

##### RemoveSwapFile(filename As String) As Boolean

remove swap file specified filename

## ifFailureReason

##### GetFailureReason() As String

return additional useful information method ifvirtualmemory interface return false

developersdevelopersbrightscriptobjectreferencehashingandstorageobjectsmd
# Hashing and Storage Objects



version older version

version

version

version

version

version

version

previous version


section describes object related local storage player registry well generating data structure hashing file

roblockcipherhashingandstorageobjectsroblockciphermd
robrightpackagehashingandstorageobjectsrobrightpackagemd
rodiskerroreventhashingandstorageobjectsrodiskerroreventmd
rodiskmonitorhashingandstorageobjectsrodiskmonitormd
rohashgeneratorhashingandstorageobjectsrohashgeneratormd
ropasskeyhashingandstorageobjectsropasskeymd
roregistryhashingandstorageobjectsroregistrymd
roregistrysectionhashingandstorageobjectsroregistrysectionmd
rosqlitedatabasehashingandstorageobjectsrosqlitedatabasemd
rosqliteeventhashingandstorageobjectsrosqliteeventmd
rosqlitestatementhashingandstorageobjectsrosqlitestatementmd
rostorageattached rostoragedetachedhashingandstorageobjectsrostorageattachedrostoragedetachedmd
rostoragehotplughashingandstorageobjectsrostoragehotplugmd
rostorageinfohashingandstorageobjectsrostorageinfomd
rovirtualmemoryhashingandstorageobjectsrovirtualmemorymd

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrobtclientmd
# roBtClient

instance object represents single client object instantiated script instead client connects player robtclientmanagerinputoutputobjectsrobtclientmanagermd object sends event attached message port creates robtclient instance javascript equivalent bsbtmanagerdevelopersplayerapisbrightscriptjavascriptobjectsbsbtmanagermd

primary purpose robtclient object transfer data player client user variable characteristic client update uservariables sends command robtclienteventinputoutputobjectsrobtclienteventmd sent attached message port state retrieved using either robtclientgetuservars method robtclienteventgetparam method update robtclientevent object queued script process robtclient object return current state

## ifBtClient

##### GetClientId() As String

retrieves uuid client associated object instance

##### SetUserVars(data As String) As Boolean

specifies data client retrieve

##### GetUserVars() As String

retrieves latest data robtclient state

##### Disconnect() As Boolean

force player disconnect client

## ifMessagePort

##### SetPort(a As Object)

post message type robtclientevent attached message port event raised whenever queue reached

## ifUserData

##### SetUserData(a As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifIdentity

##### GetIdentity() As Integer

return unique number used identify robtclientevent object originate object

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## ifFailureReason

##### GetFailureReason() As String

return additional useful information method ifbtclient interface return false

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrobtclienteventmd
# roBtClientEvent

event object generated robtclient object client update robtclient state sends command

## ifBtClientEvent

##### GetEvent() As String

return event name currently clientupdate clientcommand

##### GetParam() As String

return event data string

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrobtclientmanagermd
# roBtClientManager

object represents gatt service player act peripheral another device phone tablet act clientcentral unlike robtmanagerinputoutputobjectsrobtmanagermd allows unidirectional nonconnectable communication beaconing robtclientmanager object used facilitate twoway connectable communication provides event attached message port client connects also manages client state provides client update event time client period inactivity javascript equivalent bsbtmanagerdevelopersplayerapisbrightscriptjavascriptobjectsbsbtmanagermd

client represented robtclientinputoutputobjectsrobtclientmd object

## ifBtClientManager

##### Start(params As roAssociativeArray) As Boolean

start communication method accepts following parameter

clienttimeout amount time second client inactive disconnected

serviceuuid uuid identifies service

clientiduuid clientidentifier attribute client device connects player write unique client identifier value attribute

uservariableuuid user variable attribute attribute intended writable player client providing primary mean exchanging state data user variable written json string

commanduuid command attribute client device writes attribute event containing command string generated associated robtclient instance

deviceinfouuid attribute device information attribute readonly client

devicedatauuid attribute device data attribute used communicate available command client readonly client


note
limit byte attribute

##### Stop() As Boolean

stop communication

##### SetDeviceInfo(a As Object) As Boolean  


##### SetDeviceData(a As Object) As Boolean

## ifMessagePort

##### SetPort(a As Object)

post message type robtclientmanagereventinputoutputobjectsrobtclientmanagereventmd attached message port

## ifIdentity

##### GetIdentity() As Integer

return unique number used identify robtclientmanagereventinputoutputobjectsrobtclientmanagereventmd object originate object

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifFailureReason

##### GetFailureReason() As String

return additional useful information method ifbtclientmanager interface return false

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrobtclientmanagereventmd
# roBtClientManagerEvent

event object generated robtclientmanagerinputoutputobjectsrobtclientmanagermd object client connects disconnect player

## ifBtEvent

##### GetEvent() As String

return name event following

clientnew value returned first time client connects

clientdelete value returned client reach clienttimeout interval disconnected


##### GetClient() As roBtClient

return robtclientinputoutputobjectsrobtclientmd object client associated event

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrobtmanagermd
# roBtManager

object facilitates oneway communication beaconing robtmanager object discover whether adapter present send advertisement using adapter

javascript equivalent bsbtmanagerdevelopersplayerapisbrightscriptjavascriptobjectsbsbtmanagermd

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type robtevent attached message port message detect insertion removal bluetooth adapter

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

retrieves arbitrary object setuserdata method

## ifIdentity

##### GetIdentity() As Integer

return unique number used identify event originate object instance

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## ifBtPeripheralManager

##### GetFailureReason() As String

return additional diagnostic information method return false

##### GetAdapterList() As roArray

return array describing available bluetooth adapter entry array consists associative array containing adapter property present associative array contains single name property describes adapter name method determine bluetooth adapter connected player

##### StopAdvertising() As Boolean

stop advertisement method return true success false failure

##### GetAdvertisingList() As roArray

return array describing active bluetooth advertisement entry array consists associative array describing single advertisement associativearray value correspond property using startadvertising method also include default parameter value explicitly note uuid value returned lowercase

##### StartAdvertising(data As roAssociativeArray) As Boolean

begin transmitting beacon message method return true success false failure message contain data standard format arbitrary custom value message format specified using mode parameter required value associative array depend value parameter

modebeacon mode us simple beaconing format

beaconuuid string representation uuid 16bit 32bit 128bit format 16bit uuid must exactly four digit punctuation 32bit uuid must exactly eight digit punctuation 128bit uuid must punctuated exactly follows cd7b6f81f7384cadaebfd2a2ea36d996

beaconmajor integer specifying 2byte major value 65535

beaconminor integer specifying 2byte minor value 65535

beaconleveloptional 8bit signed integer corresponds measurement power level meter default level

beaconmanufactureroptional 2byte integer value 65535 specifying beacon manufacturer default value

connectableoptional boolean value indicating whether advertisement connectable advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot beacon advertisement persistent default

modeeddystoneurl mode us eddystoneurl format

encapsulate advertisement packet long packet startadvertising call return false getfailurereason report compressed long

txpoweroptional integer value corresponds measurement power level meter default value corresponds level 60dbm meter recommended calibration practice measure rssi circle meter beacon average measured signal strength txpower value example measuring 65dbm rssi meter yield txpower value

note txpower value modify power level bluetooth transmitter requires physical attenuation rather txpower value transmitted bluetooth client advertisement client compare value current rssi signal determine approximate distance beacon

connectableoptional boolean value indicating whether advertisement connectable advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot eddystoneurl advertisement persistent default

modeeddystoneuid mode us eddystoneuid format

namespace 10byte value expressed hexadecimal digit

instance 6byte value expressed hexadecimal digit

txpoweroptional integer value specifying power level meter default value corresponds level 60dbm meter recommended calibration practice measure meter example 65dbm rssi lead value

connectableoptional boolean value indicating whether advertisement connectable gatt service advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot eddystoneurl advertisement persistent default

modecustom mode support arbitrary custom data vendorspecific field

cutommanufacturerdataoptional associative array containing key

manufacturer 2byte integer value 65535

data robytearray instance containing data

serviceuuidoptional serviceuuid element specified either array uuid string array associative array containing uuid keyvalue pair associative array also contain data specifies servicedata robytearray instance

connectableoptional boolean value indicating whether advertisement connectable advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot custom advertisement persistent default


specify multiple advertisement pas array associative array startadvertising method advertisement sent rotation method fail advertisement incorrecttry advertisement individually call getfailurereason determine advertisement causing error

calling startadvertising method replace previous advertisement change list advertisement modifying array calling startadvertising

## Examples

script us robtmanagergetadapterlist determine bluetooth adapter available


createobjectrobtmanager
btmgetadapterlistcount print bluetooth available


script construct associative array advertising beacon format broadcast


adv1 mode beacon beaconuuid 41fac2b21c8cb41e7b01112d1016dd39e beaconmajor beaconminor
adv2 mode beacon beaconmanufacturer beaconuuid 41fac221c8cb41e7b01112d1016dd39e beaconmajor h1234 beaconminor hff01 beaconlevel

advlist adv1 adv2
bmstartadvertisingadvlist


associative array also constructed part


adv1 mode beacon
adv1append beaconuuid 41fac221c8cb41e7b01112d1016dd39e
adv1append beaconmajor 32000 beaconminor


script construct advertisement eddystoneurl format us optional txpower parameter well


adv1 mode eddystoneurl txpower


script construct customformatted advertisement


customadv createobjectrobytearray
customadvfromhexstring0215434b2eb8c28f40898e7a1e644bb13b9fa000b001c5
adv2 mode custom custommanufacturerdata manufacturer data customadv


developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrocecinterfacemd
# roCecInterface

object provides access hdmi channel

object creation rocecinterface object created parameter


createobjectrocecinterface


possible javascript apis used instead brightscriptjavascript object javascript equivalent object cecdevelopersplayerapisjavascriptapiscecmd

## IfCecInterface

##### SendRawMessage(packet As roByteArray) As Void

sends message frame data provided robytearray destination address bit first octet

system software automatically replaces high bit first octet source address also copy physical address player following message automatically prior transmission activesource inactivesource systemaudiomoderequest

note
brightsign 8255 implementation series product reply message correct data without involving script
cecmsggetcecversion

cecmsgabort

cecmsggivedevicepowerstatus

cecmsggiveosdname

cecmsggivedevicevendorid

cecmsggivefeatures

cecmsggivephysicaladdr

cecmsgusercontrolpressed

cecmsgusercontrolreleased

cecmsgreportphysicaladdr



useinitiatoraddressfrompacket method prevent system software replacing source bit

##### UseInitiatorAddressFromPacket(enable As Boolean) As Boolean

remove source address included message system software passed true method allows transmit unmodified byte

##### GetLogicalAddress() As Integer

return current logical address method return unregistered address 0x0f indicate logical address negotiated case message still sent receiver behave differently process message

##### EnableCecDebug(filename As String) As Void

enables debugging method write packet specified file

##### GetPhysicalAddress() As roByteArray

return physical address sometimes required processing message

##### PortName ()

optional

default default output platform normally hdmi1

hdmix number number hdmi output platform

earc au335 default


## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rocecrxframeevent rocectxcompleteevent attached message port

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrocecrxframeeventmd
# roCecRxFrameEvent

romessageport attached rocecinterface instance receive event type rocecrxframeevent

## ifCecRxFrameEvent

##### GetByteArray() As roByteArray

return message data robytearray

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrocectxcompleteeventmd
# roCecTxCompleteEvent

romessageport attached rocecinterface instance receive event type rocectxcompleteevent

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifCecTxCompleteEvent   

##### GetStatusByte() As Integer

return message data integer



transmission successful
unable send hardware powered
internal error
unable send line jammed
arbitration error
bittiming error
destination address acknowledged
data byte acknowledged

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrochannelmanagermd
# roChannelManager

object manage channel scanning tuning rovideoplayer method also channel scanning capability

object creation rochannelmanager object created parameter


createobjectrochannelmanager


## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifMessagePort

##### SetPort(port As roMessagePort)

## ifChannelManager

ifchannelmanager interface provides synchronous asynchronous

### Synchronous API

##### Scan(parameters As roAssociativeArray) As Boolean

performs channel scan input atsc frequency build channel based find rochannelmanager object store list channel obtained using createchanneldescriptor method described list cleared call scan default behavior overridden

channel take approximately second scan limit scope channel scan following parameter

channelmap atsc limit frequency scan either atsc

modulationtype qam64 qam256 limit modulation type scan qam64 qam256

firstrfchannel integer andor lastrfchannel integer limit scan specified range channel high channel range optional parameter

channelstore discard merge control script handle previous channel scan information default setting discard clear channel data prior scanning hand merge overwrites data channel specified scan


##### GetChannelCount() As Integer

return number found channel

##### ClearChannelData() As Boolean

clear stored channel scanning data including persists registry method also cancel asyncscan call currently running

##### GetCurrentSnr() As Integer

return centibels currently tuned channel

##### ExporttoXML() As String

serializes content channel write file used later point unit example output

##### ImportFromXML(a As String) As Boolean

retrieves channel content stored formatting controlled using version tag

example


version10 encodingutf8 standaloneyes
doctype boostserialization
boostserialization signatureserializationarchive version7
channellist classid0 trackinglevel0 version0
channelcount2channelcount
channel classid1 trackinglevel0 version0
rfchannel42rfchannel
modulationtype7modulationtype
spectralinversion0spectralinversion
majorchannelnumber1majorchannelnumber
minorchannelnumber1minorchannelnumber
channel
channel
rfchannel42rfchannel
modulationtype7modulationtype
spectralinversion0spectralinversion
majorchannelnumber1majorchannelnumber
minorchannelnumber2minorchannelnumber
channel
channellist


##### EnableScanDebug(filename As String) As Boolean

allows scan debugging written text file default debug output scan close debug file passing empty string

example


ccreateobjectrochannelmanager
cenablescandebugtmpscandebugtxt

createobjectrovideoplayer
createobjectroassociativearray
aarfchannel
aavirtualchannel
print vplayfileaa

cenablescandebug


##### CreateChannelDescriptor(a As Object) As Object

creates associative array either passed rovideoplayerplayfile method tune channel parsed metadata generated channel object based following

index



channelindex


virtual channel number string associative array



virtualchannel


channel name string



channelname kcbs


note
channel sorted internally virtual channel could channel index script implement standard channel updown behavior

entry generated array

virtualchannel

channelname

centrefrequency

modulationtype

videopid

videocodec

audiopid

audiocodec

spectralinversion

channelmap

firstrfchannel

lastrfchannel


last three entry array allow roarray parameter scan playfile first last channel value value channel scanned kind scan performed time playing channel doesnt require retuning

example


ccreateobjectrochannelmanager
aacreateobjectroassociativearray
aachannelmap
aafirstrfchannel
aalastrfchannel
cscanaa

cinfo createobjectroassociativearray
cinfochannelindex
desc ccreatechanneldescriptorcinfo
print desc

createobjectrovideoplayer
vplayfiledesc
cscandesc


### Asynchronous API

##### AsyncScan(parameters As roAssociativeArray) As Boolean

begin channel scan input return result immediately otherwise behavior parameter method identical scan completed cancelled asyncscan generates rochannelmanagerevent support ifuserdata output type event

scan complete generated upon completion scan extra data supplied

scan progress generated upon every tune performed scan getdata return percentage complete scan


##### CancelScan() As Boolean

cancel asynchronous scan currently running method generate rochannelmanagerevent

synchronous example


createobjectrochannelmanager

scan channel
createobjectroassociativearray
aachannelmap atsc
aafirstrfchannel
aalastrfchannel
cscanaa

start first channel
index
cinfo createobjectroassociativearray
cinfochannelindex index
desc ccreatechanneldescriptorcinfo

play first channel
createobjectrovideoplayer
vplayfiledesc

play second channel
index index
cinfochannelindex index
desc ccreatechanneldescriptorcinfo
vplayfiledesc



asynchronous example


createobjectrochannelmanager
createobjectromessageport
csetportp

scan channel
createobjectroassociativearray
aachannelmap atsc
aafirstrfchannel
aalastrfchannel
casyncscanaa

loop
wait2000p
goto scancomplete
goto loop

scancomplete
start first channel
index
cinfo createobjectroassociativearray
cinfochannelindex index
desc ccreatechanneldescriptorcinfo

play first channel
createobjectrovideoplayer
vplayfiledesc

rescan current channel update
descchannelstore merge
cscandesc


developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrocontrolportmd
# roControlPort

object provides support bp200bp900 button board gpio port side button brightsign player button press returned rocontrolup rocontroldown event object used configure output level connector monitor input typically led button attached gpio connector brightsign player brightsign expansion module

javascript equivalent controlportdevelopersplayerapisjavascriptapiscontrolportmd

object creation rocontrolport object created single parameter specifies port used


createobjectrocontrolport port string


port parameter following

brightsign specifies onboard gpio connector including gpio12 button

expandergpio specifies db25 connector brightsign expansion module brightsign expansion module attached object creation fail invalid returned

expanderngpio specifies usbtogpio device connected player multiple usbtogpio device controlled using separate rocontrolport instance first device corresponds expander0gpio second expander1gpio

expanderdip specifies eight switch brightsign expansion module brightsign expansion module attached object creation fail invalid returned


note
hotplugging brightsign expansion module supported

touchboardngpio retrieves event specified bp200bp900 button board event handled manner event brightsign port

touchboardnledsetup set various output option specified bp200bp900 button board

touchboardnled set bit button specified bp200bp900 button board bit indicate whether associated


note
since multiple bp200bp900 button board connected player simultaneously value specifies port enumeration board value corresponds value returned rodeviceinfogetusbtopologyobjectreferencesystemobjectsrodeviceinfomd method unspecified enumeration value synonymous button board enumeration value touchboardgpio touchboard0gpio identical

##  ifControlPort

note
button number described gpio number pin power supply ground included button numbering scheme hardware manual associated player model view mapping button pin

##### GetVersion() As String

return version number firmware either main brightsign firmware brightsign expansion module firmware responsible control port

##### EnableOutput(button As Integer) As Boolean

mark specified button output invalid button number passed false returned successful function return true output driven high depending current output state



page table pin corresponding button onboard gpio connector

##### EnableInput(button As Integer) As Boolean

mark specified button input invalid button number passed false returned successful function return true button tristated driven high externally

##### EnableAlternateFunction(button As Integer, pin\_function As String) As Boolean

enables alternate function gpio button method applies onboard gpio connector currently supported xtx44 xtx43 xdx34 xdx33 hdx24 hdx23 ho523 model

first argument specifies gpio button number second argument specifies alternate function setting following table outline possible alternate setting

gpio button number alternate function

serial1
irin1
irout hdx23 ho523

serial0 console port
serial0
serial1


model 35mm serial port hd223 xd233 support serial port

note
revert gpio button primary function specify pinfunction gpio

##### GetWholeState() As Integer

return state input attached control port bit integer individual button checked using binary operation although normally easier call isinputactive instead

##### IsInputActive(button As Integer) As Boolean

return state specified input button configured input result undefined

##### SetWholeState(state As Integer) As Boolean 

specifies desired state output attached control port bit integer individual button using binary operation although normally easier call setoutputstate instead

##### **Example**


port createobjectrocontrolport brightsign
gpio1
gpio3
gpio5
gpio7
portsetwholestategpio1 gpio2 gpio5 gpio7 turn port


##### SetOutputState(button As Integer, level As Boolean) As Boolean

configures output specified either button configured output resulting level undefined method also used configure output behavior bp200b900 button board bp200bp900 setup section detail

##### SetOutputValue(offset As Integer, bit-mask As Integer) As Boolean

configures button bp200bp900 button board method used rocontrolport object instantiated touchboardnledsetup touchboardnled parameter bp200bp900 setup section detail

##### SetOutputValues(values As roAssociativeArray) As Boolean

configures button bp200bp900 button board method used rocontrolport object instantiated touchboardnledsetup touchboardnled parameter bp200bp900 setup section detail

##### GetProperties() As roAssociativeArray

return associative array value related attached bp200bp900 button board including hardware header revision method used rocontrolport instantiated touchboardngpio parameter

##### SetPulseParams(parameters As roAssociativeArray) As Boolean

specifies period time well time slice within period pulsing gpio led property applied gpio output method passed associative array following parameter

millisecond integer specifying time period pulsing

slice integer specifying number division within millisecond time period example 500ms time period slices2 divided 250ms slice


##### SetPulse(button As Integer, bit-field As Integer) As Boolean

set offon field particular gpio slice parameter setpulseparams method determine number bit field example specifying milliseconds500 slices2 field cause button turn every millisecond period

##### RemovePulse(button As Integer) As Boolean

remove specified gpio affected pulse

## ifMessagePort

##### SetPort(port As Object)

post message type rocontrolup rocontroldowninputoutputobjectsrocontroluprocontroldownmd attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifIdentity

##### GetIdentity() As Integer

return identity value used associate rocontrolup rocontroldown event control port

note
ifidentity interface deprecated recommend using ifuserdata interface instead

##### Examples

example script applies timed pulse gpios


button flash twice second alternating fashion

gpioport createobjectrocontrolport brightsign

gpioportenableoutput2
gpioportsetoutputstate2 true

gpioportenableoutput3
gpioportsetoutputstate3 true

pulse time slice 250ms
gpioportsetpulseparams millisecond slice

button slice slice
gpioportsetpulse2

button reverse button
gpioportsetpulse3

wait
sleep10000

stop pulsing button
gpioportremovepulse2


example script enables various alternate function gpio


createobjectrocontrolport brightsign

enable serial port gpio

cenablealternatefunction0 serial1
cenablealternatefunction6 serial1

createobjectroserialport 115200
s1sendlinethis serial port

createobjectromessageport
s1setlineeventportmp
wait10000

switch serial port 35mm serial port gpio
note advised telnetssh script testing

cenablealternatefunction4 serial0
cenablealternatefunction5 serial0

createobjectroserialport 115200
ssendlinehello console

createobjectromessageport
ssetlineeventportmp
wait10000

restore normal operation serial port

cenablealternatefunction4 gpio
cenablealternatefunction5 gpio

enable input gpio

createobjectrocontrolport brightsign
cenablealternatefunction1 irin1

nexusencodings nec32
irgpio createobjectroirreceiver source gpio encoding nexusencodings

createobjectromessageport
irgpiosetportmp

wait10000

enable output gpio hdx23 ho523 onlythe xtxd model dedicated 35mm socket

cenablealternatefunction2 irout

createobjectroirtransmitter destination gpio
irsendnec32 h12345


## BP200/BP900 Setup 

send configuration bp200bp900 button board instantiate rocontrolport touchboardnledsetup parameter call setoutputvalue method method accepts integer first integer specifies three command type offset second integer field consisting bit

offset configures button board using field split four byte eight bit byte separate part configuration script byte need listed right left value byte byte byte byte

byte specifies configuration type button board currently configuration type output specified value

byte button number configured button numbered beginning value command required

byte bitfield configuration value specifies many onoff bit used bit setoutputvalue called touchboardnled instance bp200bp900 output section detail value command required field eight bit default

byte value currently always

offset disables button button board according value field button disabled individually setting bit example passing value h00000008 disable button

offset disables led button board according value field disabled individually setting bit example passing value h00000080 disable button


note
disabling button automatically disable button viceversa disable button make separate setoutputvalue call offset offset

## BP200/BP900 LED Output

control behavior individual button led instantiate rocontrolport touchboardnled parameter pas perled field setoutputvalue method method accepts integer first integer specifies button number second integer us field specify onoff behavior button size field bit determined offset byte value described section

specifies onoff behavior single cycle bp200bp900 button board approximately 11hz example want cycle every second would offset byte value bit field h3ff800 0000000000011111111111

example script set bp900 twinkle turning button different point cycle


ledcreateobjectrocontrolport touchboard0led
ledsetupcreateobjectrocontrolport touchboard0ledsetup
ledsetupsetoutputvalue0 h000b00a0
ledsetoutputvalue0 h07fe
ledsetoutputvalue1 h07fd
ledsetoutputvalue2 h07fb
ledsetoutputvalue3 h07f7
ledsetoutputvalue4 h07ef
ledsetoutputvalue5 h07df
ledsetoutputvalue6 h07bf
ledsetoutputvalue7 h077f
ledsetoutputvalue8 h06ff
ledsetoutputvalue9 h05ff
ledsetoutputvalue10 h03ff


note
controlportexampledevelopersplayerapisjavascriptapiscontrolportmd equivalent example setting bp900 twinkle javascript

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrocontroluprocontroldownmd
# roControlUp, roControlDown

object posted rocontrolportinputoutputobjectsrocontrolportmd instance configured message port input change state rocontroldown event posted input level go high rocontrolup event posted input level go high

## ifInt

##### GetInt() As Integer

retrieves number associated event

##### SetInt(value As Integer) As Void

set value event

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

## ifSourceIdentity

##### GetSourceIdentity() As Integer

retrieves identity value used associate event source rocontrolport instance

note
ifsourceidentity interface deprecated recommend using ifuserdata interface instead

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrogpiobuttonmd
# roGpioButton

object contains input rogpiocontrolport instance

## ifInt

##### GetInt() As Integer

return input event

##### SetInt(value As Integer) As Void

set input event

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrogpiocontrolportmd
# roGpioControlPort

caution
important
script rocontrolport instead rogpiocontrolport

object used control wait event brightsign generic gpio control port typically led button connected gpio port turning gpio output change voltage gpio port turning gpio output change voltage gpio port

gpio port bidirectional must programmed either input output range setwholestate method overwrite prior output setting setoutputstate take output example setwholestate method take mask example setwholestatesetwholestate21

javascript equivalent controlportdevelopersplayerapisjavascriptapiscontrolportmd

## ifMessagePort

##### SetPort(obj As Object) As Void

## ifGpioControlPort

##### IsInputActive(input\_id As Integer) As Boolean  


##### GetWholeState() As Integer  


##### SetOutputState(output\_id As Integer, onState As Boolean) As Void  


##### SetWholeState(on\_state As Integer) As Void  


##### EnableInput(input\_id As Integer) As Boolean  


##### EnableOutput(output\_id As Integer) As Boolean



#####

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroirdowneventroirrepeateventroirupeventmd
# roIRDownEvent, roIRRepeatEvent, roIRUpEvent

event object generated button input button press button repeat button release received roirreceiver object object retrieve message body input

note
roirupevent object generated iguanaworks transceiver

## ifInt

##### GetCode() As Integer

return code received roirreceiver instance

##### SetCode(a As Integer)

override code received roirreceiver instance replacing specified binary code

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifReceivedEvent

##### GetEncoding() As String

return encoding setting roirreceiver instance setting following string



supported iguanaworks transceiver

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroirreceivermd
# roIRReceiver

object support receiving arbitrary infrared remote control code using protocol javascript equivalent bsirreceiverdevelopersplayerapisbrightscriptjavascriptobjectsbsirreceivermd

object creation roirreceiver object created associative array


createobjectroirreceiver config roassociativearray


associative array contain following parameter

source string value indicating source input

irin 35mm inputoutput connector available 4kx42 xdx32 model

gpio gpio connector

iguana iguanaworks transceiver source support encoding simultaneously

tvcontroller virtual driver available brightsign builtin product read message uart drive roirreceiver object like receiver example section

encoding array indicating required encoding



supported iguanaworks transceiver


code expressed bit

bit button code

bit manufacturer code


note
manufacturer code zero code considered intended roku soundbridge remote control

roirreceiver object generate following event

roirdownevent generates button pressed

roirrepeatevent generates button repeat

roirupevent iguanaworks transceiver generates button released


##   
ifuserdata

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifMessagePort

##### SetPort(port As roMessagePort)

specifies port receive event generated roirreceiver instance

## Examples

#### Connecting a USB-C port to an IR receiver

note
ls424 platform input supported type connector also special cable required either adapter 35mm plug 35mm socket crossover custom allinone cable liteon 306300009327


2323 v112 test input output system

main
scriptlog createobjectrosystemlog display message system
msgport createobjectromessageport
gpioport createobjectrogpiocontrolport
gpioportsetportmsgport

configir createobjectroassociativearray
builtin
configirsource typec
configirencodings createobjectroarray false
configirencodings0
irrecep createobjectroirreceiver configir

typeirrecep roirreceiver
irrecepsetportmsgport
scriptlogsendline please press button remote control display code
else irrecep invalid
scriptlogsendline receiver detected please connect receiver reboot player


eventloopmsgport




eventloopmsgport object
scriptlog createobjectrosystemlog display message system
true
event wait0 msgport
scriptlogsendline received event typeevent
typeevent roirdownevent
irdata strievent
scriptlogsendline irdata





#### Creating a tvcontoller IR Receiver


configir createobjectroassociativearray
tvcontroller type
configirsource tvcontroller
configirencodings createobjectroarray false
irrecep createobjectroirreceiver configir


developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroirremotemd
# roIRRemote

object support receiving transmitting arbitrary infrared remote control code using protocol also object send pronto code command best determine required send value capture code received roirremote remote button device pressed send code

caution
important
roirremote object cannot used receive input 35mm port 4kx42 xdx32 seriesuse roirreceiver object instead

code expressed bit

bit button code

bit manufacturer code


note
note
manufacturer code zero code considered intended roku soundbridge remote control

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type roirremotepress attached message port

## ifIRRemote

##### Send(protocol as String, code as Dynamic) As Boolean

sends specified code using blaster system currently support transmission protocol pronto code method return true code successfully transmitted determine brightscript controlled device actually received

## Pronto Hex Format 

capture pronto command likely work inbuilt blaster though work iguanaworks transceivers result trailing period long ecoded properly changing period zero 0000 issue

following example sends command panasonic television using single string pronto code also provide pronto code roarray value result less work script engine


createobjectroirremote

prontohexpanasoniconstr 0000 0071 0000 0032 0080 003f 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010 0010 0010 0010 0010 0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010 0010 0030 0010 0000

irsendphc prontohexlgonstr


developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroirremotepressmd
# roIRRemotePress

message type roirremotepress generated upon press roku soundbridge remote

## ifInt

##### GetInt() As Integer

return event

##### SetInt(value As Integer) As Void

set value event

roku soundbridge remote control integer returned following value



integer command integer command
west search
east play
north next
south previous
select pause
exit
power shuffle
menu repeat
search volume
play volume
next brightness

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroirtransmitcompleteeventmd
# roIRTransmitCompleteEvent

event object generated roirtransmitterasyncsend method return information user data

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrokeyboardmd
# roKeyboard

object used wait event keyboard also used configure localization keyboard javascript equivalent keyboard

object creation rokeyboard object created parameter


createobjectrokeyboard


## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rokeyboardpress attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifKeyboardConfig

##### IsPresent() As Boolean

return true keyboard connected player method count connected device keyboard report following key enter

##### SetNumLock(on\_off As Boolean) As Boolean

set numlock state attached keyboard passed true reset state passed false

##### SetLayout(layout As String) As Boolean

specifies localized layout attached keyboard setting take effect immediately persists registry reboot following table list valid keymap parameter player default



afghanistan spain cambodia pakistan
albania ethiopia korea republic poland
armenia finland kazakhstan portugal
austria faroe island lao romania
azerbaijan france lanka serbia
bosnia herzegovina united kingdom lithuania russia
bangladesh georgia latvia sweden
belgium ghana morocco slovenia
bulgaria guinea moldova slovakia
brazil greece montenegro senegal
bhutan croatia macedonia syria
botswana hungary mali thailand
belarus ireland myanmar tajikistan
canada israel mongolia turkmenistan
congo india macao turkey
switzerland iraq maldives taiwan
cameroon iran nigeria tanzania
china iceland netherlands ukraine
czech republic italy norway united state
germany japan nepal uzbekistan
denmark kenya pitcairn vietnam
estonia kyrgyzstan philippine south africa

equivalent azerty keyboard layout

default setting

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrokeyboardpressmd
# roKeyboardPress

event object resulting user pressing keyboard returned integer value equivalent ascii code pressed

## ifInt

##### GetInt() As Integer

return ascii value press

##### SetInt(a As Integer)

set value returned getint method

returned roint32 following value



letter key number key function key misc key special key
32826
32827 backspace
32828
32829 enter
32830 print scrn 32838
32831 scrl lock 32839
32832 pausebrk 32840
32833 32841
32834 home 32842
32836 page 32843
32837 page 32846
32845
cap 32811
left arrow 32848
right arrow 32847
arrow 32850
arrow 32849

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsropowereventmd
# roPowerEvent

ropowerevent object trigger switch plugged

object creation ropowerevent object created follows


createobjectropowerevent string string object


## IfPowerEvent

getdata object

return current state requested state switched current state requested state

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsropowermanagermd
# roPowerManager

ropowermanager object used report battery state device

object creation ropowermanager object created follows


createobjectropowermanager


## ifPowerManager

##### GetPowerSource() As String

return either battery ethernet depending power source

##### GetBatteryStatus() As Object

return following value

state string return device battery status either charging discharging chargecomplete chargefault

socpercent level charge battery percentage

hardwareversion string hardware version number


##### PowerOff()

indicates charger power

##### SetPowerSwitchMode(as A String)

take either hard soft

##### GetPowerSwitchMode() As String

return whether hard soft

## ifMessagePort

##### SetPort(as A Object)

message port used message power manager

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrosequencematchermd
# roSequenceMatcher

object used send rosequencematchevent event specified byte sequence pattern matched pattern matched event posted contributing byte discarded result pattern prefix another pattern second longer pattern never matched object

object provides standard interface overloaded interface sending event message port

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rosequencematchevent attached message port

## ifSequenceMatcher

##### SetPort(a As Object)

specifies message port rosequencematchevent object posted

##### Add(pattern As Object, user\_data As Object) As Boolean

add pattern matched rosequencematcher object instance pattern specified object convertible byte sequence robytearray rostring user data pas object returned specified pattern matched

## Example


function fromhexhex string object
byte createobjectrobytearray
bytesfromhexstringhex
return byte
function

main
serial createobjectroserialport 115200
createobjectromessageport

button1seq fromhex080a01040001e000
button2seq fromhex080e01040001e000

matcher createobjectrosequencematcher
matchersetmessageportmp
matcheraddbutton1seq name button1
matcheraddbutton2seq name button2
matcheraddflibbet name flibbet
matcheraddflobbet name flobbet

serialsetmatchermatcher
stop


finished false
finished
mpwaitmessage10000
invalid
finished true
else typeev rosequencematchevent
print button evgetuserdataname
else
print unexpected event typeev





developersdevelopersbrightscriptobjectreferenceinputoutputobjectsrosequencematcheventmd
# roSequenceMatchEvent



object generated whenever rosequencematcher match specified byte sequence pattern

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned getuserdata

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferenceinputoutputobjectsroserialportmd
# roSerialPort



object control serial port player allowing transmit receive serial data javascript equivalent bsserialportdevelopersplayerapisbrightscriptjavascriptobjectsbsserialportmd

note
serialwithtelnet registry serial communication roserialport script highly unreliable pagedevelopersbrightsignregistrykeysmd information serialwithtelnet

object creation roserialport object created parameter


createobjectroserialport port dynamic baudrate integer


port integer port enumeration serial device

standard serial device including usbserial port ls424 enumerate port though port available gpio connector model enabled rocontrolportenablealternatefunction

serial device attached first port second port

communicate serial port display ho523 port

communicate usbserial device receiver port

port string multiple usbserial device connected player device specified friendly name usbfriendlyname value corresponds value returned rodeviceinfogetusbtopology method brightsign shell usblist command used discover friendly name note name guaranteed stay product version recommended

baudrate integer baud rate serial communication serial port support following baud rate 1200 1800 2400 4800 9600 19200 38400 57600 115200 230400


##### **Example**


serial1 createobjectroserialport 115200
serial2 createobjectroserialport usba1 57600


roserialport object sends following event type

rostreamlineevent line event generated whenever line string using seteol found contains string whole line object implement ifstring ifuserdata interface

rostreambyteevent byte event generated every byte received object implement ifint ifuserdata interface


## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

set sequence writing stream default value ascii value need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### SendByte(byte As Integer) As Void

writes specified byte stream

##### SendLine(string As String) As Void

writes specified character stream followed current sequence

##### SendBlock(a As Dynamic) As Void

writes specified character stream method support either string robytearray block string null byte terminate block

##### Flush()

## ifStreamReceive

##### SetLineEventPort(port As Object) As Void

set message port rostreamlineevent event posted

##### SetByteEventPort(port As Object) As Void

set message port rostreambyteevent event posted

##### SetByteArrayEventPort(port As Object) As Void

method work like setbyteeventport cause rostreambytearrayevent message posted message port data received object type example rotcpstream much efficient since data longer need delivered brightscript byte time since serial port comparatively slow possible event still contain single character

##### SetReceiveEol(eol\_sequence As String)

set sequence signify line cause rostreamlineevent delivered message port setlineeventport need value nonprinting character global functionobjectreferenceglobalfunctionsmd robytearray sequence contains byte must passed robytearray since string contain byte

byte line terminator


createobjectrobytearray
eolpush0
createobjectromessageport
client createobjectroserialport 115200
clientsetreceiveeoleol
clientsetlineeventportmp


##### SetMatcher(matcher As Object) As Boolean

instructs stream specified matcher method return true successful pas invalid method stop using specified matcher

## ifSerialControl

##### SetBaudRate(baud\_rate As Integer) As Boolean

set baud rate device supported baud rate follows 1200 1800 2400 4800 9600 19200 38400 57600 115200 230400

##### SetMode(mode As String) As Boolean

set serial mode syntax first character number data bit either second number parity none even third number stop bit

##### SetEcho(enable As Boolean) As Boolean

enables disables serial echo return true success false failure

##### SetEol(a As String)  


##### SetFlowControl(enable As Boolean) As Boolean

enables disable rtscts handshaking serial port feature currently available 4kx42 xdx32 hdx22 model

##### SetInverted(inverted As Boolean) As Boolean

inverts txrx signal level serial port allows player communicate device signaling inversion supported commonly referred port passing true method enables inversion whereas passing false disables

##### SendBreak(duration\_in\_ms As Integer) as Boolean

sends serial break set serial break condition method return true upon success false upon failure

durationinms sends continuous break

durationinms clear break state

durationinms set break condition specified period millisecond note integer accurate tenth second


## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## Example

example script wait serial event echo input received serial port shell


serial createobjectroserialport 9600
createobjectromessageport
serialsetlineeventportp

serialonly
wait0p wait forever message
iftypemsg rostreamlineevent goto serialonly accept serial message
serialsendlinemsg echo message back serial


developersdevelopersbrightscriptobjectreferenceinputoutputobjectsmd
# Input/Output Objects



version older version

version

version

version

version

version

version

previous version


section describes object enable inputoutput function hardware interface

robtclientinputoutputobjectsrobtclientmd
robtclienteventinputoutputobjectsrobtclienteventmd
robtclientmanagerinputoutputobjectsrobtclientmanagermd
robtclientmanagereventinputoutputobjectsrobtclientmanagereventmd
robtmanagerinputoutputobjectsrobtmanagermd
rocecinterfaceinputoutputobjectsrocecinterfacemd
rocecrxframeeventinputoutputobjectsrocecrxframeeventmd
rocectxcompleteeventinputoutputobjectsrocectxcompleteeventmd
rochannelmanagerinputoutputobjectsrochannelmanagermd
rocontrolportinputoutputobjectsrocontrolportmd
rocontrolup rocontroldowninputoutputobjectsrocontroluprocontroldownmd
rogpiobuttoninputoutputobjectsrogpiobuttonmd
rogpiocontrolportinputoutputobjectsrogpiocontrolportmd
roirdownevent roirrepeatevent roirupeventinputoutputobjectsroirdowneventroirrepeateventroirupeventmd
roirreceiverinputoutputobjectsroirreceivermd
roirremoteinputoutputobjectsroirremotemd
roirremotepressinputoutputobjectsroirremotepressmd
rokeyboardinputoutputobjectsrokeyboardmd
rokeyboardpressinputoutputobjectsrokeyboardpressmd
ropowereventinputoutputobjectsropowereventmd
ropowermanagerinputoutputobjectsropowermanagermd
rosequencematcherinputoutputobjectsrosequencematchermd
rosequencematcheventinputoutputobjectsrosequencematcheventmd
roserialportinputoutputobjectsroserialportmd
roirtransmitcompleteeventinputoutputobjectsroirtransmitcompleteeventmd
roirtransmitterinputoutputobjectsroirtransmittermd
rousbfilesysteminputoutputobjectsrousbfilesystemmd
rousbhidemulatorinputoutputobjectsrousbhidemulatormd
rousbhidledemulatoreventinputoutputobjectsrousbhidledemulatoreventmd
rousbpowercontrolinputoutputobjectsrousbpowercontrolmd

developersdevelopersbrightscriptobjectreferencelegacyobjectsmd
# Legacy Objects



version older version

version

version

version

version

version

version

previous version


section describes object still offered brightscript even though primary functionality replaced modern object

rortspstreameventlegacyobjectsrortspstreameventmd
rosyncpoollegacyobjectsrosyncpoolmd
rosyncpooleventlegacyobjectsrosyncpooleventmd
rosyncpoolfileslegacyobjectsrosyncpoolfilesmd
rosyncpoolprogresseventlegacyobjectsrosyncpoolprogresseventmd

developersdevelopersbrightscriptobjectreferencenetworkingobjectsmd
# Networking Objects



version older version

version

version

version

version

version

version

previous version


section describes object related networking clientserver application feed

roconfigurationelementsnetworkingobjectsroconfigurationelementsmd
rodatagrameventnetworkingobjectsrodatagrameventmd
rodatagramreceivernetworkingobjectsrodatagramreceivermd
rodatagramsendernetworkingobjectsrodatagramsendermd
rodatagramsocketnetworkingobjectsrodatagramsocketmd
rohttpeventnetworkingobjectsro
rohttpservernetworkingobjectsro
rokeystorenetworkingobjectsrokeystoremd
romediaservernetworkingobjectsromediaservermd
romediastreamernetworkingobjectsromediastreamermd
romediastreamereventnetworkingobjectsromediastreamereventmd
romimestreamnetworkingobjectsromimestreammd
romimestreameventnetworkingobjectsromimestreameventmd
ronetworkadvertisementnetworkingobjectsronetworkadvertisementmd
ronetworkattachednetworkingobjectsronetworkattachedmd
ronetworkconfigurationnetworkingobjectsronetworkconfigurationmd
ronetworkdetachednetworkingobjectsronetworkdetachedmd
ronetworkdiscoverynetworkingobjectsronetworkdiscoverymd
ronetworkhotplugnetworkingobjectsronetworkhotplugmd
ronetworkstatisticsnetworkingobjectsronetworkstatisticsmd
roopenvpnnetworkingobjectsroopenvpnmd
roptpnetworkingobjectsroptpmd
roptpeventnetworkingobjectsroptpeventmd
rorssarticlenetworkingobjectsrorssarticlemd
rorssparsernetworkingobjectsrorssparsermd
rortspstreamnetworkingobjectsrortspstreammd
rosnmpagentnetworkingobjectsrosnmpagentmd
rosnmpeventnetworkingobjectsrosnmpeventmd
rostreambyteeventnetworkingobjectsrostreambyteeventmd
rostreamconnectresulteventnetworkingobjectsrostreamconnectresulteventmd
rostreamendeventnetworkingobjectsrostreamendeventmd
rostreamlineeventnetworkingobjectsrostreamlineeventmd
rosyncmanagernetworkingobjectsrosyncmanagermd
rosyncmanagereventnetworkingobjectsrosyncmanagereventmd
rotcpconnecteventnetworkingobjectsrotcpconnecteventmd
rotcpservernetworkingobjectsrotcpservermd
rotcpstreamnetworkingobjectsrotcpstreammd
roupnpactionresultnetworkingobjectsroupnpactionresultmd
roupnpcontrollernetworkingobjectsroupnpcontrollermd
roupnpdevicenetworkingobjectsroupnpdevicemd
roupnpsearcheventnetworkingobjectsroupnpsearcheventmd
roupnpservicenetworkingobjectsroupnpservicemd
roupnpserviceeventnetworkingobjectsroupnpserviceeventmd
rourleventnetworkingobjectsrourleventmd
rourltransfernetworkingobjectsrourltransfermd

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroaudioconfigurationmd
# roAudioConfiguration

object allows mixing leveling audio stream passed audio output

object creation roaudioconfiguration object created parameter


createobjectroaudioconfiguration


## ifAudioConfiguration

##### ConfigureAudio(audio\_routing As roAssociativeArray) As Boolean

configures audio routing method fail called audio resource active rovideoplayer roaudioplayer instance return true success false failure passed associative array following parameter

mode string set audio routing mode

dynamic default mode mixing audio stream differing sampling rate cause playback fail differing volume level normalized audio stream cannot added output currently audio playing parameter associative array ignored

prerouted setting implemented firmware remove audio stream output currently audio playing additional audio routing behavior determined autolevel pcmonly srcrate parameter

autolevel string enables disables volume leveling audio output prerouted audio mode setting enabled audio stream particular output play similar volume

pcmonly string enables true disables false compressed audio support prerouted audio mode

srcrate set sample rate audio stream converted prerouted audio mode value either 44100 48000


##### GetConfiguration() As roAssociativeArray

return audio configuration information associative array

mode string audio routing mode dynamic prerouted

decodercount number available decoder

compressedcapablecount number decoder route compressed audio

autolevel boolean flag indicating whether volume leveling setting enabled

pcmonly boolean flag indicating whether compressed audio support setting enabled

srcrate sample rate audio stream converted


note
mode dynamic associative array contain mode decodercount parameter

##### GetClockStatus() As roAssociativeArray

return audio clock information spdif hdmi output

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroaudioeventmxmd
# roAudioEventMx

roaudioplayermx object generate roaudioeventmx message following value

eventmediaended

eventoverlaymediaended

eventmediaerror

eventoverlaymediaerror


medium ended event sent track finish queued track player medium error event sent queued file found exist

## ifInt

##### GetInt() As Integer

return event

##### SetInt(value As Integer) As Void

set value event

## ifAudioUserData

##### SetUserData(user\_data As String)

set user data

##### GetUserData() As String

return user data previously setuserdata either source event object return invalid data

## ifSourceIdentity

##### GetSourceIdentity() As Integer  


##### SetSourceIdentity() As Integer

note
ifsourceidentity interface deprecated recommend using ifaudiouserdata interface instead

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroaudiooutputmd
# roAudioOutput

object allows individual control audio output player javascript equivalent audiooutputdevelopersplayerapisjavascriptapisaudiooutputmd

object creation roaudiooutput object requires single output parameter upon creation


createobjectroaudiooutput output string


output parameter take following string

none

hdmi hdmi1 hdmi2 hdmi3 hdmi4 series player multiple output



spdif

analog

analogn specifies port enumeration useful model multiple analogaudio port also analog1 specify analog output model single analogaudio port

earc au335

support multiple output using port naming terminology rodeviceinfogetusbtopologyobjectreferencesystemobjectsrodeviceinfomd


create number roaudiooutput object multiple instance object represent audio output case object override another

## ifAudioOutput

##### SetVolume(a As Integer) As Boolean

set volume specified output percentage represented integer

##### SetTone(treble As Integer, bass As Integer) As Boolean

set treble bass specified output treble bass integer range 1000 1000 indicating modification audio signal increment represents change 001db

##### SetMute(a As Boolean) As Boolean

mute specified output true method false default

##### GetOutput() As String

return string roaudiooutput object created

##### SetAudioDelay(delay\_in\_milliseconds As Integer) As Boolean

delay audio specific audio output lagging decoded sample reach output delay limited 150ms less currently system software support positive delay therefore need audio ahead video need rovideoplayersetvideodelay instead

##### SetPlugState( ) As Boolean

function return true corresponding output plug false invalid plug state cannot determined current hardware version supported 90163 onwards

setvolume setmute method work conjunction volume mute functionality offered roaudioplayer roaudioplayer volume setting affect audio decoder volume audio stream sent assigned output additional level volume control enabled roaudiooutput

roaudiooutput object affect absolute volume well mute setting audio output player streaming output affected setting implemented roaudiooutput

note
control audio output connect audio player output generated roaudiooutput setpcmaudiooutputs setcompressedaudiooutputs method used rovideoplayer roaudioplayer roaudioplayer entry explanation method

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroaudioplayermd
# roAudioPlayer

audio player used play back audio file using generic ifmediatransport interface message port object send event type roaudioevent object call asynchronous word audio playback handled different thread script script continue audio playing javascript equivalent html audio

## ifMessagePort

##### SetPort(port As roMessagePort) As Void

post message type roaudioevent attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## IfIdentity

##### GetIdentity() As Integer

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## ifMediaTransport 

rovideoplayer description ifmediatransport method

## ifAudioControl

##### SetPcmAudioOutputs(outputs As Dynamic) As Boolean

specifies audio connector output audio method accepts roaudiooutput instance array roaudiooutput instance

##### SetCompressedAudioOutputs(outputs As Dynamic) As Boolean

specifies audio connector output compressed audio dolby encoded audio method accepts roaudiooutput instance array roaudiooutput instance

note
setpcmaudiooutputs setcompressedaudiooutputs method called override setting following ifaudiocontrol method setaudiooutput mapstereooutput setusbaudioport mapdigitaloutput

##### SetMultichannelAudioOutputs(array As Object) As Boolean

##### SetAudioMode(audio\_mode As Integer) As Boolean

set audio mode roaudioplayer object method accepts following value

surround

mixed stereo

audio

left

right


option apply video file option apply audio source

##### SetVolume(volume As Dynamic) As Boolean

specifies volume audio output either percentage decibel amount percentage measurement pas integer value decibel measurement pas roassociativearray containing single dbvalue float parameter decibel measurement absolute value passing specifies change audio output effective range measurement approximately decibel

volume value clipped prior setvoume101 volume return true volume mapped output usbspdifanalog

note
separate volume level stored roaudioplayer rovideoplayer

##### SetChannelVolumes(channel\_mask As Integer, volume As Integer) As Boolean

control volume individual audio channel volume command take channel mask determines channel apply volume level percentage full scale volume control work according audio channel rather output channel mask mask following bit output

left

right

left right


##### SetPreferredAudio(description As String) As Boolean

selects audio track multiple audio track stream preferred streamspresentationandwidgetobjectsrovideoplayermd section rovideoplayer page detail

##### ConfigureAudioResources() As Boolean  

##### SetAudioDelay(delay\_in\_milliseconds As Integer) As Boolean

add presentation time stamp offset audio make possible adjust file multiplexing difference delay limited 150ms less currently system software support positive delay therefore need audio ahead video need setvideodelay instead

##### SetVideoDelay(delay\_in\_milliseconds As Integer) As Boolean

add presentation time stamp offset video make possible adjust file multiplexing difference delay limited 150ms less

##### StoreEncryptionKey(a As String, b As String) As Boolean  


##### StoreObfuscatedEncryptionKey(a As String, b As String) As Boolean

#### **Deprecated Methods**

##### SetAudioOutput(audio\_output As Integer) As Boolean

##### MapStereoOutput(mapping As Integer) As Boolean

##### MapDigitalOutput(mapping As Integer) As Boolean

##### SetStereoMappingSpan(a As Integer) As Boolean

##### SetAudioStream(stream\_index As Integer) As Boolean

##### SetSpdifMute(a As Boolean) As Boolean

##### SetUsbAudioPort(a As Integer) As Boolean

##### SetAudioOutputAux(audio\_output As Integer) As Boolean

##### SetAudioModeAux(audio\_mode As Integer) As Boolean

##### MapStereoOutputAux(mapping As Integer) As Boolean  

setvolumeauxvolume integer boolean

##### SetChannelVolumesAux(channel\_mask As Integer, volume As Integer) As Boolean

##### SetAudioStreamAux(stream\_index As Integer) As Boolean

## Configuring Audio Outputs

audiovideo file playing played need call stop changing audio output

following script show setpcmaudiooutputs setcompressedaudiooutputs method conjunction roaudiooutput audiovideo player configured output decoded audio analog output compressed audio hdmi spdif output


ao1createobjectroaudiooutput analog
ao2createobjectroaudiooutput hdmi
ao3createobjectroaudiooutput spdif

a1createobjectroaudioplayer
a1setpcmaudiooutputsao1

createobjectroarray true


a1setcompressedaudiooutputsar


caution
important
case rerouting audio output audiovideo playback cause playback stop system software still responsive command exit playback audio output modification

script set audio output third analog audio port


analog3 createobjectroaudiooutput analog3
video createobjectrovideoplayer
videosetpcmaudiooutputsanalog3


script configures multiple output audio player


analogout createobjectroaudiooutput analog
hdmiout createobjectroaudiooutput hdmi

audio createobjectroaudioplayer
audiosetpcmaudiooutputsanalogout hdmiout


script set volume level individual channel


audio createobjectroaudioplayer
audiosetchannelvolumesh01 left channel
audiosetchannelvolumesh02 right channel
audiosetchannelvolumesh03 channel


## Playing Multiple Audio Files Simultaneously

multiple file well audio track video file played combination following

analog output

spdif hdmi




single file sent output given time example roaudioplayers cannot simultaneously play spdif output second attempt playfile error free output audio video stream must stopped using ifmediatransport stop stopclear call

note following multiple audiofile functionality

onboard analog audio output hdmi output clocked samplerate clock therefore different content played content must sample rate

currently single speaker supported

audio video stream played consumes finite resource amount consumed depends bitrates stream testing determine whether given audio file played time video maximum recommended usage 16mbps video file three simultaneous 160kbps stream


script play video audio hdmi file onboard analog port


hdmiout createobjectroaudiooutput hdmi
analogout createobjectroaudiooutput analog

video createobjectrovideoplayer
videosetpcmaudiooutputshdmiout

audio createobjectroaudioplayer
audiosetpcmaudiooutputsanalogout

videoplayfilevideompg
audioplayfileaudiomp3


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroaudioplayermxmd
# roAudioPlayerMx

object allows audio file well audio stream roaudioplayermx object contains internal audio player main audio playlist consists queued audio track play sequentially audio overlay play file main playlist fade occur called overlay playing next audio track start playing expected

track queued playfile fade parameter specified associative arrayobjectreferencebrightscriptcoreobjectsroassociativearraymd parameter pas playfile

filename filename track

frontporch length millisecond skip start track value default

fadeoutlocation location millisecond fade relative value frontporch frontporch value default setting fadeoutlength value nonzero fade calculated back file

fadeoutlength length fade millisecond value default

seguelocation location millisecond event trigger next audio file play location relative first audio file played seguelocation parameter included value default fadeoutlocation

backporchlocation location millisecond termination point audio track location relative first audio file played backporchlocation parameter included audio file play value default disables back porch

trackvolume relative volume audio track measured percentage specify percentage using value

eventid audio event

eventtimestamp timestamp audio event event audio file

queuenext queuing audio track parameter value queue audio file play current track

overlay overlay specification audio track parameter value fade main audio playlist playing audio track overaly overlay additional parameter

audiobedlevel volumelevel percentage main audio playlist overlay playing specify percentage using value

audiobedfadeoutlength fadeout length main audio playlist

audiobedfadeinlength fadein lenth length underlying audio track segue triggered

fadecurrentplaynext fade command parameter value fade current main audio playlist track fade designated audio file

crossfadecurrentplaynext crossfade command parameter value force immediate crossfade current main audio playlist track designated audio file

userstring string unique value roaudioplayermx instance string returned every event generated instance since current platform support multiple roaudioplayermx instance running time userstring allows script distinguish event return


following diagram illustrates timing parameter work together

attachmentsormroaudioplayermxpng

following script illustrates simple crossfade audio track


createobjectroaudioplayermx

track1 createobjectroassociativearray
track1filename file1mp3
track1fadeinlength 4000
track1fadeoutlength 4000
track1queuenext

track2 createobjectroassociativearray
track2filename file2mp3
track2fadeinlength 4000
track2fadeoutlength 4000
track2queuenext

aplayfiletrack1
aplayfiletrack2


## ifMediaTransport

rovideoplayer description ifmediatransport method

## ifAudioControl

roaudioplayer description ifaudiocontrol method

## ifSetMessagePort

##### SetPort(a As Object)

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifIdentity

##### GetIdentity() As Integer

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## ifAudioControlMx

##### SetDecoderCount(a As Integer) As Boolean

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrocanvaswidgetmd
# roCanvasWidget

object composite background color text image single rectangle allowing layer image zaxis

object creation like widget rocanvaswidget created rorectangle size position screen


createobject rocanvaswidget rorectangle object


## ifCanvasWidget

##### Hide() As Boolean

hide widget

##### Show() As Boolean

show widget

##### Raise() As Void

sends widget zorder graphic plane front surface implement ifwidget interface default widget placed graphic zorder

note
surface always drawn graphic zorder including mouse cursor closed caption scrolling tickerspresentationandwidgetobjectsrotextwidgetmd



pausegraphics resumegraphics method rovideomodepresentationandwidgetobjectsrovideomodemd object ensure multiple change graphic zorder occur simultaneously

##### Lower() As Void

sends widget bottom zorder graphic plane behind surface implement ifwidget interface default widget placed graphic zorder

##### SetRectangle(r As roRectangle) As Boolean

change size positioning widget rectangle using passed rorectangle object

##### SetLayer(content As Object, z-level As Integer) As Boolean

set content layer within widget lowest zlevel drawn first highest zlevel drawn last object content described

##### ClearLayer(z-level As Integer) As Boolean

clear specified layer

##### Clear() As Boolean

clear layer

##### EnableAutoRedraw(enable As Boolean) As Boolean

enables disables automatic redrawing widget

function enabled call setlayer clearlayer clear result redraw need change multiple layer disable auto redraw calling setlayer function

setlayer enables disables redrawing widget layer content changed autoredraw enabled call setlayer clearlayer clear result redraw batch multiple update together first suspend drawing using enableautoredrawfalse make change content finally reenable drawing using enableautoredrawtrue redraw happens separate thread enableautoredraw return almost immediately


## Object Content

content specified layer consist object object defined roassociativearray object placed roarray prior passing setlayer method currently four object type

### Background color

color aarrggbb value background color

targetrect target rectangle another roassociativearray consisting value value relative left corner widget


### Text

text string text display

targetrect rectangle text displayed

textattrs roassociativearray containing attribute applied text attribute following

font string indicating whether text displayed smallmediumlargehuge

fontsize point size used directly creating font value font automatically resizes targetrect

fontfile filename nonsystem font

halign string indicating leftcenterright alignment text line

valign string indicating topcenterbottom alignment text perpendicular line

rotation string indicating 090180270 degree rotation text

color aarrggbb value text


### Image

filename filename image

encryptionalgorithm fileencryption algorithm currently option aesctr aesctrhmac

encryptionkey decrypt image file byte array consisting bit followed bit


note
image decryptionpresentationandwidgetobjectsroimageplayermd section roimageplayer entry detail displaying encrypted image

targetrect rectangle image displayed image automatically resized target area

sourcerect source rectangle clip source image

compositionmode enter either source sourceover latter alpha blend underlying object former replaces underlying value completely

imgattrs roassociativearray containing attribute applied image

rotation string indicating 090180270 degree rotation image


### QR Codes

quick response code appear square black dot white background used encode url email address scanned using readily available software smart phone although code usually appear black white theory contrasting color

targetrect rectangle code displayed regardless aspect ratio rectangle code always squared background color fill gap

qrcode simple form contains string encode code

qrcode complex form contains array parameter code parameter following

color foreground color code default black

backgroundcolor background color code default white

rotation string indicating 090180270 degree rotation code code scan regardless rotation

qrtext contains text encode code


## Example

code contains rocanvaswidget feature outlined


rectcreateobjectrorectangle 1920 1080
cwcreateobjectrocanvaswidget rect

aacreateobjectroassociativearray
aatext primal scream
aatargetrect
aatextattrs coloraaaaaa fontmedium halignleft valigntop

aa1createobjectroassociativearray
aa1text movin followed something else followed something else followed something else followed something else
aa1targetrect
aa1textattrs colorffffff fontlarge fontfileusb1giddyupstdotf halignleft valigntop rotation90

arraycreateobjectroarray false
arraypush color 5c5d5f
arraypush filename transparentballspng
arraypushaa

aa2createobjectroassociativearray
aa2filename transparentballspng
aa2compositionmode sourceover
aa2targetrect

aa3createobjectroassociativearray
aa3qrcode
aa3targetrect

aa4createobjectroassociativearray
aa4qrcode qrtext rotation90
aa4targetrect 1200

aa5createobjectroassociativearray
aa5qrcode color964969 backgroundcolorffff77 qrtext rotation180
aa5targetrect

cwshow
cwenableautoredraw0
cwsetlayerarray
cwsetlayeraa1
cwsetlayeraa1
cwsetlayeraa3
cwsetlayeraa4
cwsetlayeraa5
cwenableautoredraw1

cwclearlayer0


##

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroclockwidgetmd
# roClockWidget

object place clock screen construction argument

object creation roclockwidget object created several parameter


createobjectroclockwidget rect rorectangle roresourcemanager displaytype integer


rect rectangle clock displayed widget pick font based size rectangle

resourcestxt file allows localization roresourcemanager object detail

displaytype date clock show screen need create widget


example


rectcreateobjectrorectangle
rescreateobjectroresourcemanager resourcestxt
ccreateobjectroclockwidget rect
cshow


resource manager passed widget us following resource within resourcestxt file display time date correctly entry


clockdateformat

clocktimeformat

clocktimeam

clocktimepm

clockdateshortmonth
janfebmaraprmayjunjulaugsepoctnovdec
clockdatelongmonth

januaryfebruarymarchaprilmayjunejulyaugustseptemberoctobernovemberdecember
clockdateshortday
sunmontuewedthufrisat
clockdatelongday
sundaymondaytuesdaywednesdaythursdayfridaysaturday


## Control Characters

following control character datetime format string


date format

abbreviated weekday name
long weekday name
abbreviated month name
full month name
month decimal
like month decimal number without leading zero
month name decimal
like month decimal number without leading zero
digit year
four digit year

time format

hour using 24hour clock
hour using 12hour clock
hour using 24hour clock single digit preceded blank
hour using 12hour clock single digit preceded blank
minute
second


## ifWidget

##### SetForegroundColor(color As Integer) As Boolean

set foreground color argb format color value converted integer passed method value hffffffff passed 4294967295 hextointeger method available core library extensionbrightscriptlanguagereferencecorelibraryextensionmd convert string integer

##### SetBackgroundColor(color As Integer) As Boolean

set background color argb format color value converted integer passed method value hffffffff passed 4294967295 hextointeger method available core library extensionbrightscriptlanguagereferencecorelibraryextensionmd convert string integer

note
bit setforegroundcolor setbgackgroundcolor value alpha parameter zero equivalent fully transparent fully nontransparent feature allows effect similar subtitle example create semitransparent black containing text video

##### SetFont(font\_filename As String) As Boolean

set fontfilename using truetype font example sdarialttf

##### SetBackgroundBitmap(bitmap\_filename As String, stretch As Boolean) As Boolean

set background bitmap image stretch true image stretched size window

##### SetBackgroundBitmap(parameters As roAssociativeArray, stretch As Boolean) As Boolean

set background bitmap image stretch true image stretched size window associative array contain following parameter

filename name image file

encryptionalgorithm fileencryption algorithm currently option aesctr aesctrhmac

encryptionkey decrypt image file byte array consisting bit followed bit


note
image decryptionpresentationandwidgetobjectsroimageplayermd section roimageplayer entry detail displaying encrypted image

##### SetSafeTextRegion(region As roRectangle) As Boolean

specifies rectangle within widget text drawn safely

##### Show() As Boolean

display widget creation widget hidden show called

##### Hide() As Boolean

hide widget

##### Raise() As Void

sends widget zorder graphic plane front surface implement ifwidget interface default widget placed graphic zorder

note
surface always drawn graphic zorder including mouse cursor closed caption scrolling tickerspresentationandwidgetobjectsrotextwidgetmd



pausegraphics resumegraphics method rovideomodepresentationandwidgetobjectsrovideomodemd object ensure multiple change graphic zorder occur simultaneously

##### Lower() As Void

sends widget bottom zorder graphic plane behind surface implement ifwidget interface default widget placed graphic zorder

##### GetFailureReason() As String

yield additional useful information function return indicates error

##### SetRectangle(r As roRectangle) As Boolean

change size positioning widget rectangle using passed rorectangle object

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohdmiinputchangedrohdmioutputchangedmd
# roHdmiInputChanged, roHdmiOutputChanged

rovideomode object generates rohdmiinputchanged rohdmioutputchanged event object whenever hotplug status hdmi input output change javascript equivalent videoinputvideoinputconfigurationhdmiinputchanged videooutputvideooutputconfigurationhotplugevent

least rohdmioutputchanged event object always generated hotplug event even quick disconnectconnect hotplug event case disconnectconnect hotplug event generate event object

## ifInt

##### GetInt() As Integer

return event

##### SetInt(value As Integer) As Void

set value event

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd
# roHtmlWidget

object embeds chromium html rendering engine rendered full screen widget display multiple rohtmlwidget instance time javascript equivalent htmlwidgetdevelopersplayerapisjavascriptapishtmlwidgetmd



rokeystoreobjectreferencenetworkingobjectsrokeystoremd object provide client certificate website rovirtualmemoryobjectreferencehashingandstorageobjectsrovirtualmemorymd object virtual memory repository chromium

## Object Creation 

rohtmlwidget object initialized rorectangle object specifies size positioning widget screen optional associative array defines property widget


createobjectrohtmlwidget rect rorectangle property roassociativearray


property rohtmlwidget instance associative array initialization equivalent method initialization many rohtmlwidget property cannot changed without reloading page produce unpredictable result changed page running recommend setting property initialization possible rather using equivalent method

caution
important
defining initialization property rohtmlwidget instance disables method instance settransform addfont setuserstylesheet available method initialization section list available method

## Initialization Parameters

associative array passed initialization following parameter

nodejsenabled bool enables nodejsdevelopershtmldevelopmentnodejsmd widget value false default

note
reloading page nodejs enabled classified undefined behavior recommended method restarting node instance destroy rebuild rohtmlwidget

focusenabled bool enables focus mousetouchscreen event value true default

mouseenabled bool enables mousetouchscreen event value false default

scrollbarenabled bool enables automatic scrollbars content viewport value false default

browser default desktopstyle scrollbars configured mobile styledevelopershtmldevelopmentdisplayinghtmlwithoutbrightauthormd well

pinchtozoomenabled bool enables pinchtozoom functionality value false default

forcegpurasterizationenabled bool enables rasterization html graphic default decision rasterization based internal chromium logic

note
setting deprecated rasterization enabled default setting property effect

canvas2daccelerationenabled bool enables canvas acceleration improve framerate html page animation cause outofmemory issue page large number offscreen canvas surface

note
setting deprecated canvas acceleration enabled default disabled setting flag false

javascriptenabled bool enables javascript widget value true default

brightsignjsobjectsenabled bool enables brightscriptjavascript objectsdevelopersplayerapisbrightscriptjavascriptobjectsmd value false default

82554 later html widget loaded httphttps protocol share local storage database html widget loaded file protocol previous release flag allow change default behavior widget loaded httphttps unshared shared change default behavior widget locally loaded file unshared shared

forcesharedstorage bool allows html widget loaded httphttps protocol share local storage loaded domain

forceunsharedstorage bool prevents html widget loaded file protocol sharing storage

transform string set screen orientation content widget note coordinate dimension rorectangle containing widget affected rotation following value accepted

identity transform widget content oriented landscape default setting

rot90 widget content rotated portrait degree clockwise

rot180 widget content rotated portrait degree clockwise

rot270 widget content rotated portrait degree clockwise


useragent string modifies default useragent string rohtmlwidget instance

string display seturl entry information using uris access file local storage

language string specifies language load page

userstylesheet string applies specified user stylesheet page widget parameter specifying file resource storage stylesheet also specified inline data

hwzdefault string specifies default hwzdevelopershtmldevelopmenthtmlvideomd behavior value default enable

storagepath string creates local storage subfolder specified directory folder used local storage application javascript storage class

storagequota string double set total size byte allotted local storage application including indexeddb brightscript integer guaranteed able represent count byte avoid using integer calculating size float double instead since represent value string also used recommended storage path specified without storage quota chromium default reserving plus total size storage device

port romessageport configures message port rohtmlwidget instance send event using initialization parameter port parameter used instead setport method ensure script catch loadstarted loadfinished loaderror event

font roarray specifies list font file accessed webpage font file specified array string filename supported font type include truetype font file open font file woff woff2

pcmaudiooutputs roarray configures audio output html widget output specified array string string name output roaudiooutput documentationpresentationandwidgetobjectsroaudiooutputmd list acceptable name

compressedaudiooutputs roarray configures compressed audio output dolby encoded audio html widget output specified array roaudiooutput instance

multichannelaudiooutputs roarray configures multichannel audio output html widget output specified array roaudiooutput instance

inspectorserver roassociativearray configures chromium inspectordevelopershtmldevelopmenthtmlbestpracticesmd widgetstarting brightsign 8531 need also enablewebinspector registry html section enable javascript console enablewebinspector allow inspector present disable reboot needed change take effect enabledisable ldws trigger reboot apply change

ipaddr string inspector address value useful player assigned address multiple network interface wish limit inspector server default value 0000 allows inspector accept connection using either address

port port inspector server


caution
important
security reason enablewebinspector used nonproduction presentation make sure disable javascript console publishing production environment chromium version found 8531 beyond javascript console information memory even connected inspector consume memory player run result crash





securityparams roassociativearray enables disables chromium security check crossorigin request local video playback http

websecurity bool enables chromium security check crossorigin request

cameraenabled bool enables webpage access camera connected player access disabled default allows support webrtc application

insecure bool instructs widget ignore security error connecting insecure http host insecure http disabled default enabling feature make player insecure suitable production environment used testing

audiocaptureenabled bool give access audio input device let chromium enumerate audio input output device


later chromium69 later several cors check added securityparamswebsecurity enablesecurityfalse disable check following registry setting instead

registry write html disablewebsecurity

write registry using roregistrysectionobjectreferencehashingandstorageobjectsroregistrysectionmd


reghtml createobjectroregistrysection html
reghtmlwritedisablewebsecurity
reghtmlflush


flag take effect rohtmlwidget instance opposed previous flag effective instance called

note
cameraenabled parameter currently supported xtx4443 xdx3433 hdx2423 ls424ls423 4kx42 model

javascriptinjection roassociativearray specifies javascript code inject different initialization point javascript code also injected runtime using injectjavascript method associative array contain three parameter described parameter value array associative array containing single keyvalue pair array must contain source source value string contain following pure javascript code path javascript file base64encoded string beginning datatextjavascriptcharsetutf8base64 mutliple source key included load order unpredictable array also contain optional world assigned following value application user mainsee page detail world parameter included array application selected default

documentcreation script soon document created behavior suitable operation

documentready script soon ready behavior equivalent domcontentloaded event firing javascript

deferred script page load finish



config
javascriptinjection
documentcreation source
documentready source 1ajs source 1bjs
deferred source





asset roarray allows rohtmlwidget instance access asset pool file exists multiple specified asset pool asset pool lowest index array precedence array entry associative array containing information asset pool

pool roassetpool asset pool containing file

collection roassetcollection manifest identifying file pool

uriprefix string prefix webpage resource retrieve pool

poolprefix string pool prefix replace prefix looking resource pool


## ifHtmlWidget

##### GetFailureReason() As String

give information member function return false

##### Hide() As Boolean

hide widget

##### Show() As Boolean

show widget

##### raise()

raise html widget graphical element screen including html widget

##### lower()

lower html widget graphical element screen

##### SetRectangle(r As roRectangle) As Boolean

change size positioning widget rectangle using passed rorectangle object

##### SetURL(URL As String) As Boolean 

display content specified using method retrieve content local storage specify file location follows filedrivedirectoryfilename example indexhtml file content folder card selected string filesdcontentindexhtml also omit drive specification select currently active drive whichever drive current autorun loaded

##### AddAuthenticationCredentials (url As String, username As String, password As String) As Boolean

tell chromium specified username password retrieving given

##### MapFilesFromAssetPool(asset\_pool As roAssetPool, asset\_collection As roAssetCollection, pool\_prefix As String, uri\_prefix As String) As Boolean 

set mapping space pool file html content deployed brightauthor typically reside pool encrypted sha1based filename mapping mechanism required allow relative uris contained html content continue working locate appropriate resource respective pool location

method bind part resource space onto pool location method accepts following argument roassetpool object containing asset roassetcollection object identifying asset semiarbitrary string uriprefix poolprefix

form fileuriprefixresourceid rewritten form poolprefixresourceid located pool name passed roassetpoolfilesgetpoolfilepath method binding occurs every instance rohtmlwidget different mapping used different bundle content

##### SetZoomLevel(scale\_factor as Float) As Boolean

adjusts scale factor displayed page default equal

##### EnablePinchToZoom(enable as Boolean) As Boolean

enables disables pinchtozoom functionality disabled default

##### EnableSecurity(enable As Dynamic) As Boolean 

deprecated securityparams initialization parameter instead

##### EnableMouseEvents(enable As Boolean) As Boolean

deprecated mouseenabled initialization parameter instead

##### SetPortrait(portrait\_mode As Boolean) As Boolean

deprecated transform initialization parameter instead

##### SetTransform(transform As String) As Boolean

set screen orientation content widget note coordinate dimension rorectangle containing widget affected rotation method accepts following string

identity transform widget content oriented landscape default setting

rot90 widget content rotated portrait degree clockwise

rot270 widget content rotated portrait degree counterclockwise


note
javascript onload event report landscape dimension window rotated setportrait settransform method application relies onload event retrieve window dimension recommend instead using rohtmlwidgettransform initialization parameter ensures html window initialized portrait dimension

##### SetAlpha(alpha As Integer) As Boolean

set overall alpha level widget default equal

##### EnableScrollbars(scrollbars As Boolean) As Boolean

deprecated scrollbarenabled initialization parameter instead

##### AddFont(filename As String) As Boolean

deprecated font initialization parameter instead

##### SetPcmAudioOutputs(outputs As roArray) As Boolean

deprecated pcmaudiooutputs initialization parameter instead

##### SetCompressedAudioOutputs(outputs As roArray) As Boolean

deprecated compressedaudiooutputs initialization parameter instead

##### SetMultichannelAudioOutputs(outputs As roArray) As Boolean

deprecated multichannelaudiooutputs initialization parameter instead

##### SetHWZDefault(default As String) As Void 

deprecated hwzdefault initialization parameter instead

##### SetVideoPlayerDefaults(defaults As roAssociativeArray) As Boolean

set default playback setting video element widget available parameter identical rovideoplayerplayfilepresentationandwidgetobjectsrovideoplayermd method default setting overwritten parameter specified individual video element

##### ForceGpuRasterization(enable As Boolean) As Boolean

deprecated rasterization enabled default calling method effect

##### EnableCanvas2dAcceleration(enable As Boolean) As Boolean

deprecated canvas2daccelerationenabled initialization parameter instead

##### SetUserStylesheet(URI As String) As Boolean 

deprecated userstylesheet initialization parameter instead

##### FlushCachedResources() As Boolean

discard resource chromium cached memory

caution
changing storage path loaded cause storage database irretrievably lost andor damaged user avoid using setlocalstoragedir setwebdatabasedir setappcachedir apis writing brightscript application
since release brightsign us single storage path webdatabase localstorage appcache storagepath parameter rohtmlwidget static initialization parameter
82354 release setlocalstoragedir setwebdatabasedir setappcachedir called rohtmlwidget path first directory used subsequent rohtmlwidget well

##### SetLocalStorageDir(file\_path As String) As Boolean

configures html storage path method take effect rohtmlwidget instance created doesnt apply rohtmlwidget instance called

note
setlocalstoragedir setwebdatabasedir setappcachedir method configure html database html best practicesdevelopershtmldevelopmenthtmlbestpracticesmd page detail

##### SetWebDatabaseDir(file\_path As String) As Boolean

configures html storage path setlocalstoragedir entry detail

method take effect rohtmlwidget instance created doesnt apply rohtmlwidget instance called

##### SetAppCacheDir(file\_path As String) As Boolean 

configures html storage path setlocalstoragedir entry detail

method take effect rohtmlwidget instance created doesnt apply rohtmlwidget instance called

##### SetLocalStorageQuota(maximum As Dynamic) As Boolean

set total size byte persistent html storage player method accept string double integer number literal represent byte number string specify larger amount storage path specified without storage quota chromium default reserving plus total size storage device

method take effect rohtmlwidget instance created doesnt apply rohtmlwidget instance called

note
setlocalstoragequota setwebstoragequota setappcachequota method configure single storage quota applies persistent html storage player html best practicesdevelopershtmldevelopmenthtmlbestpracticesmd page detail

##### SetWebDatabaseQuota(maximum As Dynamic) As Boolean

set total size byte persistent html storage player setlocalstoragequota entry detail

method take effect rohtmlwidget instance created doesnt apply rohtmlwidget instance called

##### SetAppCacheSize(maximum As Integer) As Boolean

set maximum size byte application cache changing storage size application cache clear cache rebuild cache storage depending databasespecific attribute able size unit equal page size database established creation storage unit occur following increment 1024 2048 4096 8192 16384 32768

##### EnableJavaScript(enable As Boolean) As Boolean

deprecated javascriptenabled initialization parameter instead

##### AllowJavaScriptURLs(url\_collection As roAssociativeArray)

deprecated javascriptenabled true initialization parameter javascript object enabled site

##### PostJSMessage(data As roAssociativeArray) As Boolean

post collection keyvalue pair bsmessageport javascript class javascript object brightscript tech note detail method support passing nested associative array

##### InjectJavaScript(code As String) As Boolean

immediately injects user script javascript engine passed string contain following pure javascript code path javascript file base64encoded string beginning datatextjavascriptcharsetutf8base64

method used simulate bindready option


typeevent rohtmlwidgetevent
eventgetdatareason loadfinished
hinjectjavascriptfillpasswordfields




note
changing possible binddomloaded bindready also since javascript guaranteed ready bindready callback must event invoke global function

##### StartInspectorServer(port As Integer) As Boolean

deprecated inspectorserver initialization parameter instead

##### SetUserAgent(user\_agent As String) As Boolean

deprecated useragent initialization parameter instead

##### GetUserAgent() As String

return currently active useragent string rohtmlwidget instance

##### SetUserAgentSuffix(suffix As String) As Boolean

deprecated useragent initialization parameter instead

##### SetProxy(proxy as String) As Boolean

set name address proxy server rohtmlwidget instance make http request method take effect immediately affect network operation performed component firmware string used specify either proxy location proxy file

proxy proxy address formatted hostname contain four character character used replace octet current address example address currently 19216812 proxy proxy player attempt proxy named proxy192168

proxy file proxy file located either local file system network file local filename restriction file located network file name extension hostname considered proxyserver address rather file



example
following example valid location format file
filestoragesdassetpoolabababababababa







ftpexamplefilesproxypacftpexamplefilesproxypac

filestoragesdmyproxypactxt

##### SetProxyBypass(hostnames As String) As Boolean

exempts specified host proxy configuration rohtmlwidget instance passed array consist hostnames player attempt reach specified host directly rather using proxy specified setproxy method example hostname examplecom would exempt examplecom examplecom proxy setting

##### AddProxyAuthenticationCredentials(hostname As String, username As String, password As String)

allows user proxy proxy file included method must used specify authentication parameter

##### roHtmlWidget.acceptdialog(response as String) 

accept dialog request given string request parameter added 8516

##### roHtmlWidget.rejectdialog()

reject dialog request parameter added 8516

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rohtmlwidgetevent attached message port

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## Available Methods with Initialization 

property rohtmlwidget object configured initialization ifhtmlwidget method disabled however following method still functional

hide

show

enablepinchtozoom

flushcachedresources

setuseragent

getuseragent

setuseragentsuffix

postjsmessages


## Examples 

following example show either associative array object method configure rohtmlwidget instance using local storage cache file

note technique mutually exclusive

example initialization property




width 1920
height 1080


rect createobjectrorectangle width height

config

mouseenabled true
storagepath local


html createobjectrohtmlwidget rect config

htmlshow


example method




width 1920
height 1080


rect createobjectrorectangle width height
html createobjectrohtmlwidget rect


htmlseturlurl
htmlenablemouseeventstrue
htmlsetlocalstoragedirlocal
htmlshow


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgeteventmd
# roHtmlWidgetEvent

romessageport attached rohtmlwidget receive rohtmlwidgetevent object something happens parent rohtmlwidget instance

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifHTMLWidgetEvent

##### GetData() As roAssociativeArray

return event data associative array following keyvalue pair

reason string cause event following

loadstarted html widget started loading page

loadfinished html widget completed loading page

loaderror html widget failed load page identify failing resource message retrieve explanatory text

downloadrequest html widget instance received download request chromium instance process download request mime type doesnt recognize pdfs instead pass event along mimetype parameter brightscript autorun processing

newwindowrequest html widget instance received request open window request normally come html anchor targetblanktargettop javascript windowopen method requested specified parameter

javascriptdialog string html widget instance received javascript alert confirmation brightscript respond calling rohtmlwidget acceptdialogresponseasstring rejectdialog method rohtmlwidgetrohtmlwidgetacceptdialogresponseasstringpresentationandwidgetobjectsrohtmlwidgetmd response provided within second rohtmlwidget auto reject dialog attempt apis called dialog request rohtmlwidget effect parameter added 8516

message string message javascript dialog display applicable reasonjavascriptdialog explanatory text related load failure applicable reasonloaderror property exists multiple event type different meaning different event type

defaulttext string javascript prompt dialog asks user enter text default text displayed input field field empty dialog type applicable reasonjavascriptdialog parameter added 8516

type dialog type javascriptdialog event either alert confirm prompt onbeforeunload event applicable reasonjavascriptdialog parameter added 8516

securityorigin string security origin request applicable reasonjavascriptdialog parameter added 8516

string failing resource newwindow request applicable reasonloaderror reasonnewwindowrequest

mimetype string mime type download request applicable reasondownloadrequest

string download request applicable reasondownloadrequest


## Example

following event loop wait html widget event event indicates download request received script pass relevant data createpdfrenderer function defined


true
wait0 gaamp
print received event typeev
typeev rohtmlwidgetevent
eventdata evgetdata
typeeventdata roassociativearray typeeventdatareason rostring
eventdatareason loaderror
print html load error eventdatamessage
else eventdatareason loadfinished
print received load finished
receivedloadfinished true
else eventdatareason message
msgportpostbsmessagetext message
else eventdatareason loadstarted
print received load started
else eventdatareason downloadrequest
print received download request
eventdatamimetype applicationpdf
createpdfrendererfileindexhtmlfile eventdataurl
endif
else
print unhandled html event
print eventdatareason
endif
else
print unknown eventdata typeeventdata
endif
endif
endwhile


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroimagebuffermd
# roImageBuffer

object allows access decoded imagefile data copy manipulate data

object creation roimagebuffer object instantiated roimageplayer object string specifying file path image file roimageplayer object needed invalid substituted


createobjectroimagebuffer imageplayer object filepath string


example


imgbuffer createobjectroimagebuffer invalid sdcontentimagepng


## ifImageBufferControl

##### DisplayBuffer(x As Integer, y As Integer) As Boolean

display image screen integer specify coordinate topleft corner image

caution
important
displaybuffer method deprecated point exists perform function

##### GetBufferByteArray() As roByteArray

return decoded imagefile data robytearray

##### GetBufferMetadata() As roAssociativeArray

return associative array containing information image file associative array contains following key

width width image file

height height image file

acceptable boolean integer value indicating whether image displayed roimageplayer instance

format color space argbcmyk image file


##### ConvertFormat(a As String) As Object

#####

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroimageplayermd
# roImagePlayer

object display static bitmap image video display simplest roimageplayer make call displayfile filename string alternatively preloadfile conjunction displaypreload control pleasing aesthetic generating image player roimagewidget object javascript equivalent html

object creation image player displayed first creating rorectangle roimageplayer instance calling setrectangle using rorectangle instance argument


rectangle createobjectrorectangle 1024
createobjectroimageplayer
isetrectanglerectangle


## ifImageControl 

##### DisplayFile(image\_filename As String) As Boolean

display image specified filename imagefilename string must point jpeg 8bit 24bit 32bit file note jpeg image file cmyk color profile supported

##### DisplayFile(parameters As roAssociativeArray) As Boolean

display image using associative array display parameter

filename name image file

mode image mode entry setdefaultmode detail

transition image transition setting entry setdefaulttransition detail

encryptionalgorithm fileencryption algorithm currently option aesctr aesctrhmac

encryptionkey decrypt image file byte array consisting bit followed bit


image decryption section detail displaying encrypted image

caution
important
image player longer accepts encryption key bottom bit identical

##### PreloadFile(image\_filename As String) As Boolean

load specified image file offscreen memory buffer

##### PreloadFile(parameters As roAssociativeArray) As Boolean

load image file offscreen memory buffer image display property determined associative array parameter

filename name image file

mode entry setdefaultmode detail

transition entry setdefaulttransition detail


##### DisplayPreload() As Boolean

us onscreen memory buffer display image stored offscreen memory buffer using preloadfile memory buffer displayed screen used preloading image preloadfilecan called multiple time displaypreload called keep loading offscreen buffer displayfile method call preloadfile followed immediately displaypreload previously preloaded image lost image preloaded displaypreload effect

##### StopDisplay() As Boolean

remove image display

##### DisplayFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean  


##### PreloadFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean

##### SetDefaultMode(mode As Integer) As Boolean

set default image display mode displayfile preloadfile setdefaultmode called default mode equivalent image centered without scaling supported display mode listed

center image scaling take place cropping occurs image bigger window

scale image scaled fully viewable aspect ratio maintained

scale fill crop image scaled completely fill window aspect ratio maintained

scale fill image stretched fill window whole image viewable aspect ratio maintained different window


##### SetDefaultTransition(transition As Integer) As Boolean

set transition used next image displayed following available transition

transition immediate blit

wipe bottom left right

explodes centre left right bottom left bottom right

1011 us vertical horizontal venetianblind effect

1213 comb vertical horizontal

fade background color back

fade current image image

1619 slide bottom left right

2023 slide entire screen bottom left right

2425 scale image work pseudo rotation around vertical horizontal axis

2629 expands image onto screen right left bottom


##### SetTransform(transform As String) As Boolean

applies eight transforms image call method take effect next file displayed note image rectangle change accommodate height width ratio transformed image method called separately multiple roimageplayer roimagewidget instance

identity transformation default behavior

rot90 degree clockwise rotation

rot180 degree rotation

rot270 degree clockwise rotation

mirror horizontal mirror transformation

mirrorrot90 mirrored degree clockwise rotation

mirrorrot180 mirrored degree clockwise rotation

mirrorrot270 mirrored degree clockwise rotation


##### OverlayImage(image\_filename As String, x As Integer, y As Integer) As Boolean

composite image specified filename primary displayfile image integer specify location within image widget

##### SetRectangle(r As roRectangle) As Boolean

change size positioning image rectangle using passed rorectangle object

##### GetRectangle() As roRectangle

return rorectangle object location dimension rorectangle object used define image window

##### CreateTestHole(hole As roRectangle) As Boolean

creates hole image location dimension specified passed rorectangle instance video window located directly beneath image show method disrupt image playback used test purpose

##### SetTransitionDuration(duration As Integer) As Boolean

set amount time take millisecond specified transition effect take place default transition duration 1000 millisecond

##### DisplayBuffer(a As Object, b As Integer, c As Integer) As Boolean  


##### Hide() As Boolean

hide image currently displayed roimageplayer widget

##### Show() As Boolean

show image currently displayed roimageplayer widget

##### Raise() As Void

sends widget zorder graphic plane front surface implement ifwidget interface default widget placed graphic zorder

note
surface always drawn graphic zorder including mouse cursor closed caption scrolling tickerspresentationandwidgetobjectsrotextwidgetmd



pausegraphics resumegraphics method rovideomodepresentationandwidgetobjectsrovideomodemd object ensure multiple change graphic zorder occur simultaneously

##### Lower() As Void

sends widget bottom zorder graphic plane behind surface implement ifwidget interface default widget placed graphic zorder

## X, Y

value indicate position image center near possible us center image point position nearest center

display image zone setrectangle must called enablezonesupport must included script zone functionality

## Testing Display Modes

example shell command test different display mode


brightsign image filenamebmp
brightsign image filenamebmp
brightsign image filenamebmp
brightsign image filenamebmp

brightsign image filenamebmp
brightsign image filenamebmp


## Preloading Images

following example script us preloaded image improve speed user hit keyboard soon struck display switch image already preloaded possible delay occurs image preloading case image display soon loaded


createobjectroimageplayer
createobjectromessageport
createobjectrokeyboard
ksetportp

ipreloadfileonebmp

loop
idisplaypreload
ipreloadfiletwobmp
wait0p
idisplaypreload
ipreloadfileonebmp
wait0p
goto loop


## Image Decryption 

roimageplayer roimagewidget roclockwidget rotextwidget rocanvaswidget object used display encrypted image object image playback method accepts associative array include encryptionalgorithm encryptionkey decryption parameter

note
contact supportbrightsignbizmailtosupportbrightsignbiz learn generating obfuscation storing player

call rodeviceinfohasfeaturemediadecryption determine player model firmware version support image decryption

example


print play encrypted image image widget

imageplayer createobjectroimagewidget

aacreateobjectroassociativearray
aafilename sdimagesencjpg
aaencryptionalgorithm aesctr
aaencryptionkey createobjectrobytearray
aaencryptionkeyfromhexstring01030507090b0d0f00020406080a0c0e00000000000000000000000000000000

imageplayerdisplayfileaa
sleep10000
imageplayerhide

print play encrypted image playstaticimage

videoplayer createobjectrovideoplayer

aacreateobjectroassociativearray
aafilename sdimagesencjpg
aaencryptionalgorithm aesctr
aaencryptionkey createobjectrobytearray
aaencryptionkeyfromhexstring01030507090b0d0f00020406080a0c0e00000000000000000000000000000000

videoplayerplaystaticimageaa
sleep10000
videoplayer invalid

print show clock image

resourcemanager createobjectroresourcemanager sdresourcestxt

clockwidget createobjectroclockwidget resourcemanager

aacreateobjectroassociativearray
aafilename sdimagesencjpg
aaencryptionalgorithm aesctr
aaencryptionkey createobjectrobytearray
aaencryptionkeyfromhexstring01030507090b0d0f00020406080a0c0e00000000000000000000000000000000

clockwidgetsetbackgroundbitmapaa true
clockwidgetshow
sleep10000
clockwidgethide

print text widget encrypted background image

twparams createobjectroassociativearray
twparamslinecount
twparamstextmode
twparamsrotation
twparamsalignment

twcreateobjectrotextwidgetr112twparams
twsetbackgroundcolorh00ff0000
twsetforegroundcolorhff00ff00
twpushstringencrypted background
twsetrectangler

aacreateobjectroassociativearray
aafilename sdimagesencjpg
aaencryptionalgorithm aesctr
aaencryptionkey createobjectrobytearray
aaencryptionkeyfromhexstring01030507090b0d0f00020406080a0c0e00000000000000000000000000000000

twsetbackgroundbitmapaa true
twshow
sleep10000
twhide

cwcreateobjectrocanvaswidget rect
canvasaacreateobjectroassociativearray
canvasaafilename sdimagesencjpg
canvasaaencryptionalgorithm aesctr
canvasaaencryptionkey createobjectrobytearray
canvasaaencryptionkeyfromhexstring01030507090b0d0f00020406080a0c0e00000000000000000000000000000000
cwsetlayercanvasaa
cwshow


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsroimagewidgetmd
# roImageWidget

object used place roimageplayer case image displayed within rectangle using roimagewidget result pleasing aesthetic image player creation also used display image multiscreen array beyond roimagewidget behaves identically roimageplayer javascript equivalent html

object creation image widget area generated using rorectangle object


rectangle createobjectrorectangle 1024
createobjectroimagewidget rectangle


## ifImageControl 

##### DisplayFile(image\_filename As String) As Boolean

display image specified filename imagefilename string must point jpeg 8bit 24bit 32bit file note jpeg image file cmyk color profile supported

##### DisplayFile(parameters As roAssociativeArray) As Boolean

display image using associative array display parameter

filename name image file

mode image mode entry setdefaultmode detail

transition image transition setting entry setdefaulttransition detail

encryptionalgorithm fileencryption algorithm currently option aesctr aesctrhmac

encryptionkey decrypt image file byte array consisting bit followed bit


image decryptionpresentationandwidgetobjectsroimageplayermd descrption roimageplayer entry detail displaying encrypted image

##### PreloadFile(image\_filename As String) As Boolean

load specified image file offscreen memory buffer

##### PreloadFile(parameters As roAssociativeArray) As Boolean

load image file offscreen memory buffer image display property determined associative array parameter

filename name image file

mode entry setdefaultmode detail

transition entry setdefaulttransition detail


##### DisplayPreload() As Boolean

us onscreen memory buffer display image stored offscreen memory buffer using preloadfile memory buffer displayed screen used preloading image preloadfilecan called multiple time displaypreload called keep loading offscreen buffer displayfile method call preloadfile followed immediately displaypreload previously preloaded image lost image preloaded displaypreload effect

##### StopDisplay() As Boolean

remove image display

##### DisplayFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean  


##### PreloadFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean

##### SetDefaultMode(mode As Integer) As Boolean

set default image display mode displayfile preloadfile setdefaultmode called default mode equivalent image centered without scaling supported display mode listed

center image scaling take place cropping occurs image bigger window

scale image scaled fully viewable aspect ratio maintained

scale fill crop image scaled completely fill window aspect ratio maintained

scale fill image stretched fill window whole image viewable aspect ratio maintained different window


##### SetDefaultTransition(transition As Integer) As Boolean

set transition used next image displayed following available transition

transition immediate blit

wipe bottom left right

explodes centre left right bottom left bottom right

1011 us vertical horizontal venetianblind effect

1213 comb vertical horizontal

fade background color back

fade current image image

1619 slide bottom left right

2023 slide entire screen bottom left right

2425 scale image work pseudo rotation around vertical horizontal axis

2629 expands image onto screen right left bottom


##### SetTransform(transform As String) As Boolean

applies eight transforms image call method take effect next file displayed note image rectangle change accommodate height width ratio transformed image method called separately multiple roimageplayer roimagewidget instance

identity transformation default behavior

rot90 degree clockwise rotation

rot180 degree rotation

rot270 degree clockwise rotation

mirror horizontal mirror transformation

mirrorrot90 mirrored degree clockwise rotation

mirrorrot180 mirrored degree clockwise rotation

mirrorrot270 mirrored degree clockwise rotation


##### OverlayImage(image\_filename As String, x As Integer, y As Integer) As Boolean

composite image specified filename primary displayfile image integer specify location within image widget

##### SetRectangle(r As roRectangle) As Boolean

change size positioning image rectangle using passed rorectangle object

##### GetRectangle() As roRectangle

return rorectangle object location dimension rorectangle object used define image window

##### CreateTestHole(hole As roRectangle) As Boolean

creates hole image location dimension specified passed rorectangle instance video window located directly beneath image show method disrupt image playback used test purpose

##### SetTransitionDuration(duration As Integer) As Boolean

set amount time take millisecond specified transition effect take place default transition duration 1000 millisecond

##### DisplayBuffer(a As Object, b As Integer, c As Integer) As Boolean

##### Hide() As Boolean

hide image currently displayed roimagewidget instance

##### Show() As Boolean

show image currently displayed roimagewidget instance

## Multiscreen Images

object includes overloaded preloadfile displayfile method method receive roassociativearray object store various option passed must used displaying image across multiple screen array displaying portion imagethough also used place original method call case

following code us preloadfile method multiscreen display


icreateobjectroimagewidget
acreateobjectroassociativearray
afilename testjpg
amode
atransition
amultiscreenwidth
amultiscreenheight
amultiscreenx
amultiscreeny
ipreloadfilea
idisplaypreload


filename mode transition value documented displayfile preloadfile method multiscreenwidth multiscreenheight parameter specify width height multiscreen matrix example would three screen wide screen high multiscreenx multiscreeny specify position current screen within matrix

case average image drawn screen though image mode still applies depending shape image black bar side screen relatively simple therefore image widget display part image based position multiscreen array following default value parameter

mode

transition

multiscreenwidth

multiscreenheight

multiscreenx

multiscreeny


code us displayfile display portion image


icreateobjectroimagewidget
acreateobjectroassociativearray
afilename testjpg
amode
asourcex
asourcey
asourcewidth
asourceheight
idisplayfilea


display portion image test starting coordinate sourcex sourcey sourcewidth sourceheight size viewmode still honored displaying whole file

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsronodejsmd
# roNodeJs

ronodejs brightscript object allows launching nodejs instance nodejs instance access brightsign nodejs module built module ronodejs also provides mechanism communicate javascript brightscript environment complex application

## Object Creation

ronodejs instantiated filename optional parameter


node createobjectronodejs indexjs messageportmymessageport argument arg1 arg2


8217 later version also pas optional nodearguments parameter provides argument node interpreter opposed argument provides argument javascript application inside node


node createobjectronodejs indexjs messageportmymessageport nodearguments argument arg1 arg2


messageport optional allows communication javascript application

argument optional pass argument node instance

nodearguments optional pass argument nodejs executable example enable remote inspector nodejs nodearguments take multiple argument

envvars optional pass environment variable supplied associative array nodejs application note environment variable name casesensitive roassociativearray caseinsensitive default brightscript literal syntax associative array force name lower case ensure correct behavior call setmodecasesensitive addreplace method variable array following example slightly less verbose addreplace




asetmodecasesensitive
akey
akey
print return


## PostJsMessage()

postjsmessage data associativearray boolean
post collection keyvalue pair brightscript messageport javascript class method take associative array doesnt support nested associative array javascript brightscript detail

## roNodeJs Events

page information ronodejs event

## Examples

enable inspector using nodearguments


nodejs createobjectronodejs mainjs messageport msgport nodearguments inspect00002999 argumentsnodeapplicationargument1 nodeapplicationargument2


change directory directory current javascript file


procchdirdirname


timer stop node exiting


setintervalfunctionconsolelogping 10000


pas argument ronodejs


node createobjectronodejs indexjs
nodearguments dotenvconfig argument dotenvconfigpathstoragesdenv


note nodearguments argument come filename argument come filename

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsronodejseventmd
# roNodeJsEvent

romessageport attached ronodejs receive ronodejsevent object something happens parent ronodejs instance

## ifUserData

setuserdatauserdata object
set user data returned event raised

getuserdata object
return user data previously setuserdata return invalid data

## ifNodeJsEvent

getdata roassociativearray
return event data associative array following keyvalue pair

reason string cause event following

processexit nodejs instance exited

message nodejs instance sent message

exitcode number field present value reason field value processexit return exit code nodejs process described exitcode field defined onwards note nodejs script could also code purpose

message string reason field value message field return content message


## Example

following event loop wait nodejs event report event


true
wait0 gaamp
print received event typeev
typeev ronodejsevent
eventdata evgetdata
typeeventdata roassociativearray typeeventdatareason rostring
eventdatareason processexit
print nodejs instance exited code eventdataexitcode
else eventdatareason message
print received message eventdatamessage
msgportpostbsmessagetext message
else
print unhandled nodejs event
print eventdatareason
endif
else
print unknown eventdata typeeventdata
endif
endif
endwhile


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrorectanglemd
# roRectangle

object passed various video graphic widget rovideoplayer roimagewidget rohtmlwidget specify size positioning

object creation object created coordinate dimension parameter


createobjectrorectangle integer integer width integer height integer


setrectangle call made widget object roimagewidgetsetrectangle honor viewmode aspectratio conversion mode user user video player letterboxing occur video rectangle exactly

### Rectangles with 4K Video Modes 

player using video mode 3840x2160x60p rectangle still operate total screen area 1920x1080 unless fullresolution graphicspresentationandwidgetobjectsrovideomodemd enabled scaled factor video output example display fullscreen video rorectangle instance 0019201080 display additional video topright quadrant screen another rorectangle instance 9600960540

attachments4k20coordinatespng

note video output pixel ratio graphic element roimagewidget rocanvaswidget upscaled match size video output occurs irrespective size original image widget rectangle example image 960x540 rectangle first downscaled 960x540 upscaled 1920x1080 want display image without upscaling video mode display video window using rovideoplayerplaystaticimage method enable fullresolution graphicspresentationandwidgetobjectsrovideomodemd

## ifRectangle

##### SetX(x As Integer) As Void

specifies coordinate rectangle

##### SetY(y As Integer) As Void

specifies coordinate rectangle

##### SetWidth(width As Integer) As Void

specifies width value rectangle

##### SetHeight(height As Integer) As Void

specifies height value rectangle

##### GetX() As Integer

return coordinate rectangle

##### GetY() As Integer

return coordinate rectangle

##### GetWidth() As Integer

return width rectangle

##### GetHeight() As Integer

return height rectangle

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrostreamqueuemd
# roStreamQueue

object allows play list video file seamlessly without blank frame interrupt video next link rostreamqueue rovideoplayer instance seamless video playback romediastreamer instance seamless video streaming

object creation object created parameter


createobjectrostreamqueue


## File Requirements

video file must meet following requirement work rostreamqueue object

file must transport stream formatted

file queue identical pid

file must begin closed

file must regular pcrs interval 100ms shorter note default interval ffmpeg 1000ms unless configured muxing case interval 20ms following example appropriate commandline remux



avconv clipshortts vcodec copy acodec copy muxrate clipshort2ts


## ifStreamQueue

##### QueueFile(filename As String) As Boolean

add specified video file queue

##### Loop(loop As Boolean) As Boolean

specifies playbackstreaming return beginning queue reach loopfalse looplastfalse called playbackstreaming stop queue reached also default behavior

##### LoopLast(loop\_last As Boolean) As Boolean

specifies playbackstreaming loop last file queue reach method effect looptrue called well

##### SetPreferredAudio(description As String) As Boolean

chooses video stream video input based parameter passed string

##### SetPreferredVideo(description As String) As Boolean

chooses audio stream video input based parameter passed string

##### KeepPadding(enabled As Boolean)

enabledtrue pid input stream including padding packet passed output allows bitstream profile preserved restreaming network cannot used feeding local decoder

##### NextFile(a As Boolean) As Boolean  


##### Start() As Boolean

## ifMessagePort

##### SetPort(port As roMessagePort)

post message type rostreamqueueevent attached message port event raised whenever queue reached

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifIdentity

##### GetIdentity() As Integer

return unique number used identify event originate object

note
ifidentity interface deprecated recommend using ifuserdata interface instead

## Playing and Streaming Queues

rostreamqueue streaming playlist include source component romediastreamersetpipeline call video playback rovideoplayer instance destination component setpipeline call

##### **Example (roVideoPlayer)**


qcreateobjectrostreamqueue
qqueuefilesdtestcountupblueframests
qqueuefilesdtestcountupgreenframests
qlooptrue
ccreateobjectromediastreamer
rcreateobjectrorectangle0019201080
vcreateobjectrovideoplayer
vsetrectangler
csetpipelineq
cstart


##### **Example (roMediaStreamer)**


queue createobjectrostreamqueue
queuequeuefilefile1ts
queuequeuefilefile2ts
queuelooptrue
createobjectromediastreamer
msetpipelinequeue udp23901561015000maxbitrate0
mstart


caution
important
strongly suggest appending maxbitrate0 parameter stream using rostreamqueue prevents romediastreamer instance ratelimiting rostreamqueue stream already running precise correct rate

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrostreamqueueeventmd
# roStreamQueueEvent

event object generated rostreamqueue object queue reached

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

## ifStreamQueueEvent

##### GetData() As Object

return roassociativearray entry action file

action contains

start indicates playback queued file started

skip indicates file queue skipped

indicates file finished playing

file contains name file whose state returned action

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotextfieldmd
# roTextField

text field represents area screen contain arbitrary text feature intended presenting diagnostic usage information rotextwidget object generate text user interface signage

object creation object created several parameter


createobjectrotextfield xpos integer ypos integer widthinchars integer heightinchars integer metadata object


xpos horizontal coordinate left text field

ypos vertical coordinate left text field screen equivalent zero

widthinchars width text field character cell

heightinchars height text field character cell

metadata optional roassociativearray containing extra parameter text field pas zero require


metadata associative array support following extra parameter

charwidth width character cell pixel

charlength height character cell pixel

backgroundcolor background color text field integer specifying eight bit green blue form hrrggbb

textcolor color text integer specifying eight bit green blue form hrrggbb

size alternative charwidth charlength specifying either normal size text doublesized text


note
mode border around screen displayed overscanning want rovideomode object function getsafex getsafey ensure coordinate visible

## ifTextField

##### Cls() As Void

clear text field

##### GetWidth() As Integer

return width text field

##### GetHeight() As Integer

return height text field

##### SetCursorPos(x As Integer, y As Integer) As Void

move cursor specified position subsequent output appear position

##### GetValue() As Integer

return value character currently cursor

##### Raise() As Void

sends widget zorder graphic plane front surface implement ifwidget interface default widget placed graphic zorder

note
surface always drawn graphic zorder including mouse cursor closed caption scrolling tickerspresentationandwidgetobjectsrotextwidgetmd



pausegraphics resumegraphics method rovideomodepresentationandwidgetobjectsrovideomodemd object ensure multiple change graphic zorder occur simultaneously

##### Lower() As Void

sends widget bottom zorder graphic plane behind surface implement ifwidget interface default widget placed graphic zorder

## ifStreamSend

##### SendByte(byte As Integer) As Void

writes character indicated specified number current cursor position within text field advance cursor

##### SendLine(string As String) As Void

writes character specified current cursor position followed endofline sequence

##### SendBlock(string As Dynamic) As Void

writes character specified current cursor position advance cursor position beyond last character method support either string robytearray block string null byte terminate block

##### SetSendEol(string As String) As Void

set sequence sent sendline value leave default ascii value carriage return normal need change value another nonprinting character global functionobjectreferenceglobalfunctionsmd

note
ifstreamsend interface also described section documenting various file object interface described manner specific rotextfield object

## Printing a Text Field 

object implement ifstreamsend interface text field written using print textfield syntax example detail

also possible write text field using syntax print textfield character position textfield example textfield object column row writing position writes column position position position 1623 last

output reach bottom text field automatically scroll

##### **Example**


meta createobjectroassociativearray
metaaddreplacecharwidth
metaaddreplacecharlength
metaaddreplacebackgroundcolor h101010 dark grey
metaaddreplacetextcolor hffff00 yellow
createobjectrovideomode
createobjectrotextfield vmgetsafex vmgetsafey meta
print hello world
tfsetcursorpos4
print world hello


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotextwidgetmd
# roTextWidget

object used display text screen

note scrolling ticker mode limited ticker time rotextwidgets long mode example static text

object creation object created using variant

option


createobjectrotextwidget rorectangle linecount integer textmode integer pausetime integer


rorectangle instance contains text

linecount number line text show within rectangle

textmode animation characteristic text

animated view similar teletype

static text

simple text queue string

scrolling ticker string separated diamond default separator modified using setseparator method note option available lsx22 hdx20 hdx10 model

pausetime length time string displayed displaying next string apply text mode string screen updated immediately


option


createobjectrotextwidget rorectangle linecount integer textmode integer parameter roassociativearray


rorectangle instance contains text

linecount number line text show within rectangle

textmode animation characteristic text

animated view similar teletype

static text

simple text queue string

scrolling ticker string separated diamond default separator modified using setseparator method note option available lsx22 hdx20 hdx10 model

parameter associative array include following value

linecount number line text show within rectangle

textmode animation characteristic text

animated view similar teletype

static text

simple text queue string

scrolling ticker string separated diamond default separator modified using setseparator method note option available lsx22 hdx20 hdx10 model

pausetime length time string displayed displaying next string apply text mode string screen updated immediately

rotation rotation text within widget note coordinate dimension rectangle rotated

degree

degree value also represented degree radian

degree value also represented degree radian

degree value also represented degree radian

alignment alignment text

left

center

right




mode useful displaying feed tickertype text however dynamic data immediate screen update required mode appropriate mode allows text drawn immediately screen

note
textmode scrolling ticker support righttoleft lefttoright arabic hebrew scrolling mode depending language first string file added widget change scrolling direction first need remove string ticker

## ifTextWidget

##### SetGlobalParameter(param As String, value as Integer) As Void

configures parameter related scrolling ticker text mode following accepted parameter

startat starting position scrolling text number left side screen total width widget start right side screen offscreen specify value total width widget

autopop autopop setting widget value string automatically removed popped stack scrolled offscreen value default behavior string automatically removed

autoaddseparator separator setting widget setting value disables string separator useful displaying emojis pushsurface method setting value enables string separator default behavior

pixel string string separator beginning string default value parameter reliable ticker contains string memory


note
global parameter altered show called case startat parameter result undefined parameter autopop autoaddseparator intended used show called

##### GetGlobalParameter(param as String) As Integer

return value parameter using setglobalparameter method method also return value readonly laststringid parameter unique identifier string recently added listlist value identical integer returned pushstring pushsurface method

##### PushString(str As String) As Boolean

add string list element display mode string displayed order reached object loop returning beginning list mode string displayed immediately method return unique identifier used rotextwidgetevent message determine string moved offscreen failure element list return

note
adding many string without popping stack cause pushstring return false exact number depends font size string maximum recommended number stored string

##### PushSurface(image as roImageBuffer) As Integer

add bitmap image list element display mode image scaled match height ticker method return unique identifier used rotextwidgetevent message determine imagesurface moved offscreen failure element list return

note
currently restriction formatting recommended color format main screen

##### PopStrings(number\_of\_string\_to\_pop As Integer) As Boolean

pop element front list using last first ordering mode occurs next time widget wrap element added removed widget seamlessly mode element cleared widget immediately

##### GetStringCount() As Integer

return number element exist pending pop taken place

##### Clear() As Boolean

clear list element leaving widget blank able accept pushstring call

##### SetStringSource(file\_path As String) As Boolean

display text file specified path single continuous string method applicable text mode scrolling ticker file reached text widget loop beginning using diamond symbol separator

##### SetAnimationSpeed(speed As Integer) As Boolean

set speed animated text display method applicable text mode

mode default speed value 10000 setting integer value decrease speed teletypestyle ticker example specifying value 20000 decrease default speed text display half value 5000 double default speed

mode default speed value 10000 speed scrolling ticker measured pixel second speed must multiple current framerate else rounded nearest multiple example framerate honor value software determines speed scrolling ticker performing following calculation passed speed parameter
speed 10000


##### SetSeparator(separator As String) As Boolean

change separator string default diamond separator replaced content passed string method applies text mode smooth scrolling ticker following string indicate special symbol diamond circle square

##### SetSyncManager(domain As String) As Boolean

specifies rosyncmanagerobjectreferencenetworkingobjectsrosyncmanagermd domain executing setmultiscreen call method called creates internal domain based existing rosyncmanager domain us network parameter recommend using method instead passing multicast address port setmultiscreen method

##### SetMultiscreen(offset As Integer, size As Integer, ip\_address As String, port As Integer) As Boolean

display smooth scrolling ticker across multiple screen specify network synchronization parameter either call setsyncmanager method first pas optional ipaddress port value setmultiscreen method calling setsyncmanager preferred setsyncmanager specify ipaddressport lead unexpected behavior

master screen designated instance rightmost offset player multiscreen array pushstring show call well change must made master instance follower instance text widget remain blank leader start method requires following parameter

offset offset pixel display multiscreen array example using offset 1920 twoscreen array 1920x1080 screen would specify player righthand master display

size total width pixel multiscreen array example defining size 3840 would specify twoscreen array 1920x1080 screen

ipaddress string specifying multicast address rosyncmanagerobjectreferencenetworkingobjectsrosyncmanagermd network traffic 23919200

port string specifying multicast port synchronization process 1234


note
player support multiscreen ticker time

## ifWidget

##### Show() As Boolean

display widget creation widget hidden show called

##### Hide() As Boolean

hide widget

##### Raise() As Void

sends widget zorder graphic plane front surface implement ifwidget interface default widget placed graphic zorder

note
surface always drawn graphic zorder including mouse cursor closed caption scrolling ticker



pausegraphics resumegraphics method rovideomodepresentationandwidgetobjectsrovideomodemd object ensure multiple change graphic zorder occur simultaneously

##### Lower() As Void

sends widget bottom zorder graphic plane behind surface implement ifwidget interface default widget placed graphic zorder

##### SetForegroundColor(color As Integer) As Boolean

set foreground color argb format bit alpha parameter zero equivalent fully transparent fully nontransparent

note
foreground alpha value currently unsupported ticker mode scrolling ticker ignored method behavior change future firmware version

color value converted integer passed method value hffffffff passed 4294967295 hextointeger method available core library extensionbrightscriptlanguagereferencecorelibraryextensionmd convert string integer

##### SetBackgroundColor(color As Integer) As Boolean

set background color argb format bit alpha parameter zero equivalent fully transparent fully nontransparent feature allows effect similar subtitle example create semitransparent black containing text video

color value converted integer passed method value hffffffff passed 4294967295 hextointeger method available core library extensionbrightscriptlanguagereferencecorelibraryextensionmd convert string integer

##### SetFont(font\_filename As String) As Boolean

specifies custom font widget using truetype font file local storage sdcomicsansttf

##### SetBackgroundBitmap(bitmap\_filename As String, stretch As Boolean) As Boolean

set background bitmap image stretch true image stretched size widget

##### SetBackgroundBitmap(parameters As roAssociativeArray, stretch As Boolean) As Boolean

set background bitmap image stretch true image stretched size widget associative array contain following parameter

filename name image file

encryptionalgorithm fileencryption algorithm currently option aesctr aesctrhmac

encryptionkey decrypt image file byte array consisting bit followed bit


note
image decryptionpresentationandwidgetobjectsroimageplayermd section roimageplayer entry detail displaying encrypted image

##### SetSafeTextRegion(region As roRectangle) As Boolean

specifies rectangle within widget text drawn safely

##### SetRectangle(r As roRectangle) As Boolean

change size positioning widget rectangle using passed rorectangle object

##### GetFailureReason() As String

yield additional useful information function return indicates error

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotextwidgeteventmd
# roTextWidgetEvent

event object generated string surface leaf screen area rotextwidget instance

## ifWidgetEvent

##### GetStringId() As Integer

return string surface disappeared screen

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Objecta

return user data previously setuserdata either event source object return invalid data

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotoucheventrotouchcalibrationeventmd
# roTouchEvent, roTouchCalibrationEvent

rotouchevent object generated rotouchscreen object whenever touch mouse event detected within defined region javascript equivalent touchevent

## ifInt

##### GetInt() As Integer

retrieves region event

##### SetInt(a As Integer)

set region event

## ifPoint

ifpoint interface available rotouchcalibrationevent object

##### GetX() As Integer

retrieves coordinate mousetouch event

##### GetY() As Integer

retrieves coordinate mousetouch event

##### SetX(a As Integer)

set coordinate event

##### SetY(a As Integer)

set coordinate event

## ifEvent

ifevent interface available rotouchcalibrationevent object

##### GetEvent() As Integer  


##### SetEvent(a As Integer)

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotouchscreenmd
# roTouchScreen

object accepts input touchscreen panel mouse recognized input object generate rotouchevent object rotouchscreen section brightscriptjavascript migration guidedevelopersplayerapisbrightscriptjavascriptmigrationguidemd equivalent method javascript

touchscreen supported please page full list supported touchscreen rotouchscreen object responds click mouse responds touch event touchscreen

touchscreenmouse interactivity follow outline

create rotouchscreen instance

setport specify romessageport instance receive rotouchscreen event

define touch region

touch region rectangular circular

touch click occurs anywhere inside area touch region event sent message port

touch region overlap click touch hit multiple region event affected region sent

process event


rotouchscreen object support rollover region rollover based around touch region rectangular circular region added default rollover enablerollover method image region whenever mouse cursor within region image displayed case image displayed allows button highlighted mouse cursor move

## ifTouchScreen

##### SetResolution(x As Integer, y As Integer) As Void  


##### AddRectangleRegion(x As Integer, y As Integer, w As Integer, h As Integer, region\_id As Integer) As Void

add rectangular touch region screen regionid used associate touch region rotouchevent event link region rollover image

##### AddCircleRegion(x As Integer, y As Integer, radius As Integer, region\_id As Integer) As Void

add circular touch region screen regionid used associate touch region rotouchevent event link region rollover image

##### ClearRegions() As Void

clear list region added using addrectangleregion addcircleregion contact region longer generate event call effect rollover graphic

##### GetDeviceName() As String  


##### SetCursorPosition(x As Integer, y As Integer) As Void  


##### SetCursorBitmap(filename As String, x As Integer, y As Integer) As Void 

specifies file mouse cursor icon method also accepts spot point within icon rectangle trigger event mouse clicked coordinate icon rectangle width height

##### EnableCursor(enable As Boolean) As Void

display cursor screen passed true

##### EnableRollover(region\_id As Integer, on\_image As String, off\_image As String, cache\_image As Boolean, image\_player As Object) As Void

enables rollover touch region method accepts touch region well string specifying name bitmap image cache setting image player draw rollover cacheimage parameter simply tell script whether keep bitmap loaded memory setting us memory quickly recommend cacheimage normally

##### SetRollOverOrigin(region\_id As Integer, x As Integer, y As Integer) As Void

change origin less screen change mouse roll region mean bitmap larger region drawn default requirement rollover bitmap size position touch region note bitmap square circular region default origin circular region center circle radius

caution
important
enablerollover setrolloverorigin method deprecated point exist perform function

##### EnableRegion(region\_id As Integer, enabled As Boolean) As Void

enables disables rollover region method accepts touch region well boolean value true false rollover region default enabled created region start script enable region required

##### IsMousePresent() As Boolean

return true relative pointing device attached player work absolute device like touchscreen

##### SetMouseRotation(rotation As Integer) As Boolean

transforms mousemovement input account screen rotation method accept following integer

input unchanged landscape orientation

rotated degree clockwise portrait orientation

rotated degree

rotated degree counterclockwise portrait orientation


##### EnableSerialTouchscreen(a As Integer) As Boolean  


##### SetSerialTouchscreenConfiguration(a As String) As Boolean

##### GetDiagnosticInfo() As String

return html string captured information describing hardware connected event occurred calibration process method used calibration script diagnose touchscreen issue

## ifSetMessagePort

##### SetPort(port As roMessagePort)

post message type rotouchevent rotouchcalibrationevent attached message port

## ifTouchScreenCalibration

##### StartCalibration() As Boolean  


##### GetCalibrationStatus() As Integer  


##### GetDiagnosticInfo() As String  


##### ClearStoredCalibration() As Boolean  


##### StartEventLogging() As Boolean  


##### StopEventLogging() As Boolean  


##### ClearEventLogs() As Boolean

##### SetCalibrationRanges(x-min As Integer, x-max As Integer, y-min As Integer, y-max As Integer) As Boolean

override screen range value provided touchscreen method useful entirety video output displayed touch surface practical method usually requires custom calibration script appropriate image calibration setting matched particular setup

## ifSerialControl

##### SetBaudRate(baud\_rate As Integer) As Boolean

set baud rate device supported baud rate follows 1200 1800 2400 4800 9600 19200 38400 57600 115200 230400

##### NotUsed1(a As String)  


##### SetMode(a As String) As Boolean  


##### NotUsed2(a As Boolean) As Boolean

## Examples

script loop video wait mouse click touchscreen input output coordinate click touch shell located within defined region


vcreateobjectrovideoplayer
tcreateobjectrotouchscreen
pcreateobjectromessageport

vsetportp
tsetportp
vsetloopmodetrue
vplayfiletestclipmp2v

taddrectangleregion001001002

loop
msgwait0
print type typemsg
print msgmsg
typemsgrotouchevent
print xymsggetxmsggety
endif
goto loop


script includes mouse support


tcreateobjectrotouchscreen
tsetportp
put cursor mouse attached
cursor must
position spot point
tsetcursorbitmapcursorbmp
tsetresolution1024
tsetcursorposition512

pas enable cursor display true false
cursor enable mouse attached

tenablecursortrue


script includes rollover region mouse support


imgcreateobjectroimageplayer
tcreateobjectrotouchscreen
pcreateobjectromessageport
tsetportp


tsetcursorbitmapcursorbmp
tsetresolution1024
tsetcursorposition512
tenablecursortrue


imgdisplayfilemenubmp


add rectangular touch region
enables rollover support region
set rollover origin position touch region
taddrectangleregion0
tenablerollover1 onbmp offbmp true
tsetrolloverorigin1


#####

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideoeventroaudioeventmd
# roVideoEvent, roAudioEvent

video audio event declared separate class event following value retrieved using getint method



playing current medium item started playing
mediaended medium item completed playback
timehit particular timecode reached entry timecode eventspresentationandwidgetobjectsrovideoplayermd detail
overlayplaying roaudioplayermx instance begun playback audio file
overlaymediaended roaudioplayermx instance completed playback audio file
overlaytimehit eventtimestamp roaudioplayermx instance reached
mediaerror medium error detected opposed code event usually indicates transient error buffer level
overlaymediaerror medium error detected roaudioplayermx playback
fadingout current medium item completed fading rovideoplayersetfade entry detail
decodereos
overlayfadingout fadeoutlocation roaudioplayermx instance reached
overlaydecodereos
underflow stream seems underflowing event usually indicates streaming latency generated every second long underflow detected
mediaerrornotstarted fatal error encountered attempting start playback video format supported
resourceshortage trying play video simultaneously allowed playing single video creating video tag reuse existing video possible avoid race condition video might hold onto hardware video resource take long disassociate video player video



note
diagnostic server return specific information medium error state

## ifInt

##### GetInt() As Integer

return event integer value

##### SetInt(value As Integer) As Void

set integer value

## ifUserData

##### SetUserData(user\_data As Object) As Void

set user data

##### GetUserData() As Object

return user data previously setuserdata either event source object return invalid data

## ifSourceIdentity

##### GetSourceIdentity() As Integer  


##### SetSourceIdentity() As Integer 

note
ifsourceidentity interface deprecated recommend using ifuserdata interface instead

## ifData    

##### GetData() As Integer

##### SetData(a As Integer) 

## Example


vpmsgloop
msgwaittiut
typemsgrovideoevent
debug print video eventmsggetint
msggetint
debug print videofinished
retcode5
return
endif
else typemsgrogpiobutton
debug print button pressmsg
escm msgbm retcode1return
esc1 msgb1 retcode2return
esc2 msgb2 retcode3return
esc3 msgb3 retcode4return
else typemsgrotint32
debug print timeout
retcode6
return
endif

goto vpmsgloop


developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideoinputmd
# roVideoInput

object allows playback hdmi input video provided video capture dongle note ifvideoinput method apply hdmi input achieved passing unmodified rovideoinput instance rovideoplayerplayfile method example javascript equivalent mediadevicesgetusermedia

object creation rovideoinput created parameter


createobjectrovideoinput


## ifVideoInput

##### GetStandards() As roArray

##### GetInputs() As roArray

return array string describing various input video standard video capture device support following possible standard returned paldk palg palh pali pald pald1 palk palm paln palnc pal60 secambg ecamb secamd secamg secamh secamk secamk1 secaml secamlc secamdk ntscm ntscmj ntsc443 ntscmk palb palb1 input returned svideo composite

##### SetStandard(standard As String) As Boolean  


##### GetCurrentStandard() As String  


##### SetInput(input As String) As Boolean  


##### GetCurrentInput() As String

input video standard

##### GetControls() As roArray

return possible control input include brightness contrast saturation others

##### SetControlValue(control\_name As String, value As Integer) As Boolean

set value specified control

##### GetCurrentControlValue(control\_name As String) As roAssociativeArray

return associative array member value minimum maximum value current value possible range specified minimum maximum

##### GetFormats() As Object  


##### SetFormat(a As String, b As Integer, c As Integer) As Boolean  


##### GetCurrentFormat() As String

## Examples

script us hdmi input video source create fullscreen display


createobjectrovideoplayer
createobjectrovideoinput
createobjectromessageport


createobjectrovideomode
vmsetmode1920x1080x60p


createobjectrorectangle 1920 1080
vsetrectangler


vplayfilei


script us video capture dongle video source create fullscreen display


vcreateobjectrovideoplayer
icreateobjectrovideoinput
pcreateobjectromessageport


vmcreateobjectrovideomode
vmsetmode1280x720x60p


createobjectrorectangle 1280
vsetrectangler


isetinputsvideo
isetstandardntscm


vplayfilei


#####

developersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsmd
# Presentation and Widget Objects



version older version

version

version

version

version

version

version

previous version


section describes object relate directly audiovideo playback brightsign player

roaudioconfigurationpresentationandwidgetobjectsroaudioconfigurationmd
roaudioeventmxpresentationandwidgetobjectsroaudioeventmxmd
roaudiooutputpresentationandwidgetobjectsroaudiooutputmd
roaudioplayerpresentationandwidgetobjectsroaudioplayermd
roaudioplayermxpresentationandwidgetobjectsroaudioplayermxmd
rocanvaswidgetpresentationandwidgetobjectsrocanvaswidgetmd
roclockwidgetpresentationandwidgetobjectsroclockwidgetmd
rohdmiinputchanged rohdmioutputchangedpresentationandwidgetobjectsrohdmiinputchangedrohdmioutputchangedmd
rohtmlwidgetpresentationandwidgetobjectsrohtmlwidgetmd
rohtmlwidgeteventpresentationandwidgetobjectsrohtmlwidgeteventmd
roimagebufferpresentationandwidgetobjectsroimagebuffermd
roimageplayerpresentationandwidgetobjectsroimageplayermd
roimagewidgetpresentationandwidgetobjectsroimagewidgetmd
ronodejspresentationandwidgetobjectsronodejsmd
ronodejseventpresentationandwidgetobjectsronodejseventmd
rorectanglepresentationandwidgetobjectsrorectanglemd
rostreamqueuepresentationandwidgetobjectsrostreamqueuemd
rostreamqueueeventpresentationandwidgetobjectsrostreamqueueeventmd
rotextfieldpresentationandwidgetobjectsrotextfieldmd
rotextwidgeteventpresentationandwidgetobjectsrotextwidgeteventmd
rotextwidgetpresentationandwidgetobjectsrotextwidgetmd
rotouchevent rotouchcalibrationeventpresentationandwidgetobjectsrotoucheventrotouchcalibrationeventmd
rotouchscreenpresentationandwidgetobjectsrotouchscreenmd
rovideoevent roaudioeventpresentationandwidgetobjectsrovideoeventroaudioeventmd
rovideoinputpresentationandwidgetobjectsrovideoinputmd
rovideomodepresentationandwidgetobjectsrovideomodemd
rovideoplayerpresentationandwidgetobjectsrovideoplayermd

developersdevelopersbrightscriptobjectreferencesystemobjectsrodevicecustomizationmd
# roDeviceCustomization



version older version

version

version

version

version

version

version

previous version


object provides miscellaneous device configuration customization method

## ifFailureReason

##### GetFailureReason() As String

return helpful information ifdevicecustomization method fail

## ifDeviceCustomization

##### WriteSplashScreen(filename As String) As Boolean

remove default splash screen previously splash screen replaces specified image file image file must supported format method return true success false failure

##### EnumerateExtensions() As Array

return array extension installed player

##### FactoryReset(confirm As String) As Boolean

applies factory reset player method must passed string confirm work otherwise return false nothing successful method reboot without return value following step carried factory reset

file wiped boot drive including custom splash screen autorun script

value wiped registry

reset player

flash drive wiped


##### ConfigureAsUsbGadget(roBool gadget)

method allows port au335 dynamically configured host gadget mode host role port follows standard behavior allows device plugged gadget role player behave device example rousbfilesystem method return false platform au335

script switch gadget role present sdtestimg filesystem connected host


dccreateobjectrodevicecustomization
dcconfigureasusbgadget1

createobjectrousbfilesystem
fsenablefilename sdtestimg


configureasusbgadget1 isnt called au335 host mode regardless connected

note brightsign player au335 port doesnt need configuration work mode stack switch automatically host gadget depending connected port

##### EncryptStorage(device As String, params As roAssociativeArray) As Boolean

encrypts content storage device using encryption stored private section player registry prevents device reading name content file storage device though file metadata still readable storage device still mounted device list delete copy file even though cannot read

device parameter specify storage drive encrypt hereobjectreferencehashingandstorageobjectsrostorageinfomd list valid drive name encryption parameter passed associative array contain following

method stringrequired encryption method following

none encryption disabled encryption key storage device deleted registry

passphrase storage device encrypted using unobfuscated passphrase

obfuscatedpassphrase storage device encrypted using obfuscated passphrase contact supportbrightsignbiz learn generating obfuscation storing player

brightsignkey storage device encrypted using encryption common brightsign player shared outside party

generatekey storage device encrypted using encryption generated ondemand using secure random generator private registry player contains copy value registry erased becomes corrupted recover data storage device

note private registry distinguish different physical volume drive example encrypt card first card overwritten second card encrypted case randomly generated data first card irretrievable

passphrase string passphrase encrypting storage device parameter must included method specified passphrase obfuscatedpassphrase

format boolean setting parameter true cause specified storage device reformattedall existing file deleted guaranteed securely erased device encrypted however device cannot reformatted operation fail parameter false storage device mounted previously encrypted using supplied

storage device hasnt previously encrypted encrypted leaving preexisting file unencrypted storage device encrypted using different operation fail

format parameter specified storage device mounted previously encrypted using supplied storage device hasnt previously encrypted operation fail

developersdevelopersbrightscriptobjectreferencesystemobjectsrodeviceinfomd
# roDeviceInfo



version older version

version

version

version

version

version

version

previous version


object provides information device hardware firmware feature javascript equivalent deviceinfodevelopersplayerapisjavascriptapisdeviceinfomd

## ifDeviceInfo

##### GetModel() As String

return model name brightsign device running script string example hd1020 xd230

##### GetVersion() As String

return version number brightsign firmware running device example 4013

##### GetVersionNumber() As Integer

return three significant version number brightsign firmware running device comparable numeric form major65536 minor256 build

caution
important
return value getversionnumber method include additional version number first three example firmware version 40134 returned 262157 4013 reason recommend using getversion firmwareisatleast method determine current firmware version

##### FirmwareIsAtLeast(version As String) As Boolean

return true brightsign firmware version device greater equal version number represented passed string 4013

##### GetBootVersion() As String

return version number brightsign boot firmware also known safe mode string example

##### GetBootVersionNumber() As Integer

return three significant version number brightsign boot firmware also known safe mode comparable numeric form major65536 minor256 build

caution
important
return value getbootversionnumber method include additional version number first three example firmware version 1041 returned 65540 reason recommend using getbootversion bootfirmwareisatleast method determine current boot firmware version

##### BootFirmwareIsAtLeast(version As String) As Boolean

return true brightsign boot firmware version device greater equal version number represented passed string 4422

##### GetTemperature() As roAssociativeArray

return associative array containing dynamic string location temperature floating point value

##### GetDeviceUptime() As Integer

return number second device running since last power cycle reboot

##### GetDeviceLifetime() As Integer

##### GetLoadStatistics(parameters As roAssociativeArray) As String

provides current performance information related linux kernel method accepts associative array single keyvalue pair formatted itemparameter return string containing information associated parameter following recognized parameter

loadavg provides information system performance first three column measure utilization past minute respectively fourth column display number currently running process total number process last column display recently used process

meminfo display physical swap memory usage

slabinfo provides information memory usage slab level

stat provides overall statistic system number page fault since system booted

vmstat display detailed virtual memory statistic kernel

zoneinfo provides overall statistic system broken system node

interrupt display interrupt many type

version provides kernel version


example


stat createobjectrodeviceinfo
print statgetloadstatisticsiteminterrupts


##### GetUSBTopology(return As roAssociativeArray) As Dynamic 

return topology player including port enumeration device method determine whether certain device connected certain port passed associative array determines return value

return topology string list

format true return topology xmlformatted string

format array return array associative array associative array contains information single port

rebuild true ensures returned information date current hardware status


update information return format


createobjectrodeviceinfo
digetusbtopologyformat rebuildtrue


string list


brightscript debugger createobjectrodeviceinfo
brightscript debugger topo digetusbtopology
brightscript debugger print topo

container

category

1552

type
1507


device

category

ident usbhiddev0
60931
11210
type bp900
2127




string


brightscript debugger createobjectrodeviceinfo
brightscript debugger topo digetusbtopologyxml true
brightscript debugger print topo
topology
device
raw8110raw
fidc0fid
categoryhidcategory
vid084fvid
pidee03pid
identusbhiddev0ident
typebp900type
device
device raw214 categoryhub vid05e3 pid0610
device
raw214110raw
fida40fid
categoryaudiocategory
vid05a7vid
pid40fapid
device
device
raw214112raw
fida42fid
categoryhidcategory
vid05a7vid
pid40fapid
device



array


brightscript debugger createobjectrodeviceinfo
brightscript debugger topo digetusbtopologyarray true
brightscript debugger print topo0
05a7
40fa

category audio
214110
ident usbhiddev0


port device connected include friendly value array xmlstring return include value determine physical port player device connected following table match value port different model line

model family friendly location

ls424ls423 front usbc
hdx24hdx23 front usba
hs123 connector
ho523 upper front usba
lower front usba
back tx25
xdx33xdx34 front usbc
back usba
xtx43xtx44 back usba
front usbc

value portint indicates device directly connected player value portintint indicates device connected last integer specifies endpoint example device present audio device listed separate device different endpoint number also note layer port number multiple hub connected together a400

##### GetDeviceUniqueId() As String

return identifier empty string unique unit running script

##### GetFamily() As String

return single string indicates family device belongs device family model capable running firmware

##### HasFeature(feature As String) As Boolean

return true player feature passed caseinsensitive string parameter present current device firmware possible feature queried script listed

caution
important
pas parameter listed return false even feature available hardware firmware

serial serial port

audio1 first audio output

audio2 second audio output

audio3 third audio output

brightscript1 brightscript version

brightscript2 brightscript version

component video component video output

ethernet ethernet interface

findmemberfunction global function name available globalfunctions page detail

gpio connector da15 phoenixstyle gpio port

hdmi hdmi output

hdmi input hdmi input

hevcdecode h265 video decoder

mediadecryption ability decrypt aesencrypted medium including video image audio file

nand storage nand storage boot loader firmware

networking form networking capability false return indicate network currently available

reset button reset button

registry onboard persistent storage

realtime clock

sdhccompatible storage

sdhc sdhccompatible storage

serial port first serial port

serial port second serial port

serial port third serial port

button service button passing legacy term gpio12 button yield result

interface

output

videoencoder video encodertranscoder


example


createobjectrodeviceinfo
print digetmodel
print digetversion digetversionnumber
print digetbootversion digetbootversionnumber
print digetdeviceuptime digetdevicebootcount


particular system generate following


hd1010
3241 197161
3228 197148
14353 3129


developersdevelopersbrightscriptobjectreferencesystemobjectsroelectronmd
# roElectron



version older version

version

version

version

version

version

version

previous version


brightscript object launch electron instance brightscript runtime

brightsign javascript object available electron brightsign mechanism allow communication javascript electron main process brightscript brightsign process

note
object available series player

## Object Creation

roelectron take parameter filename option parameter


createobjectroassociativearray
aamessageport mymessageport
aaarguments createobjectroarray
aaarguments0 arg1
aaarguments1 arg2
aanodearguments createobjectroarray
aanodearguments nodearg1 nodearg2
aaenvvars createobjectroassociativearray
aaenvvarsaddreplaceenvvar1 test
aaenvvarsaddreplaceenvvar2 true
node createobjectroelectron pathtomyapplication


messageport optional message port bridge electron brightscript application

argument optional roarray argument electron

nodearguments optional roarray argument electron application consume

envvars optional roassociativearray environment variable electron application


brightscript associative array case insensitive objectliteral syntax example aabrightsign used environment variable generally considered case sensitive addreplace method associative array call setmodecasesensitive assigning objectliteral syntax variable envvars associative array

## Methods

##### PostJSMessage(data as AssociativeArray) as Boolean

post collection keyvalue pair brightscript messageport javascript class method take associative array doesnt support nested associative array javascript brightscript detail

## Events

roelectroneventsystemobjectsroelectroneventmd information roelectron event

developersdevelopersbrightscriptobjectreferencesystemobjectsroelectroneventmd
# roElectronEvent



version older version

version

version

version

version

version

version

previous version


romessageport attached roelectron object receive roelectronevent object something happens parent roelectron instance

## ifUserData

##### SetUserData(user\_data As Object)

set user data returned event raised

##### GetUserData() As Object

return user data previously setuserdata return invalid data

## ifElectronEvent

##### GetData() As roAssociativeArray

return event data associative array following keyvalue pair

reason string cause event following

processexit electron instance exited

message electron instance sent message


exitcode number value field electron application exit electron process exit code defined later version note electron script also code purpose

message string reason field value message field return content message


## Example

following event loop wait electron event report event


true
wait0 gaamp
print received event typeev
typeev roelectronevent
eventdata evgetdata
typeeventdata roassociativearray typeeventdatareason rostring
eventdatareason processexit
print electron instance exited code eventdataexitcode
else eventdatareason message
print received message eventdatamessage
msgportpostbsmessagetext message
else
print unhandled electron event
print eventdatareason
endif
else
print unknown eventdata typeeventdata
endif
endif
endwhile


developersdevelopersbrightscriptobjectreferencesystemobjectsroresourcemanagermd
# roResourceManager



version older version

version

version

version

version

version

version

previous version


roresourcemanager object used manage string multiple language

object creation roresourcemanager object created single filename parameter specifies name file contains localized resource string required user file must utf8 format


createobjectroresourcemanager filename string


## ifResourceManager

##### SetLanguage(language\_identifier As String) As Boolean

instructs roresourcemanager object specified language false returned resource associated specified language

##### GetResource(resource\_identifier As String) As String

return resource string current language given resource identifier

##### GetFailureReason() As String

yield additional useful information function return indicates error

##### GetLanguage() As String

## Usage

present roresourcemanager primarily used localizing roclockwidget resource file passed creation following format string entry


resourceidentifiernamegoeshere
janfebmaraprmayjunjulaugsepoctnovdec
janfebmraprmaijunjulaugsepoktnovdez
enefebmarabrmayjunjulagosepoctnovdic
janfvmaravrmaijunjulaousepoctnovdc
genfebmaraprmaggiulugagosetottnovdic
janfebmaraprmeijunjulaugsepoktnovdec
janfebmaraprmajjunjulaugsepoktnovdec


name square bracket resource identifier line language identifier followed resource string multiple roresourcemanager object created default resourcestxt file contains range internationalization value clock widget available page

developersdevelopersbrightscriptobjectreferencesystemobjectsrosystemlogmd
# roSystemLog



version older version

version

version

version

version

version

version

previous version


object enables recording system brightsign player note brightscript print value written system ifstreamsend method write instead

object creation object created parameter


createobjectrosystemlog


## ifSystemLog

##### ReadLog() As roArray

return array string string correspond line system spanning bootup recent entry

##### ReadNextLine() As String

read next line recorded system

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

set sequence writing stream default value crlf need value nonprinting character global functionobjectreferenceglobalfunctionsmd

##### SendByte(byte As Integer) As Void

writes specified byte stream

##### SendLine(string As String) As Void

writes specified character stream followed current sequence

##### SendBlock(a As Dynamic) As Void

writes specified character stream method support either string robytearray block string null byte terminate block

##### Flush() As Void

writes stream file blocking execution data written

## Writing to a Remote Syslog Server

brightsign player write remote syslog server using standard syslog protocol 3164 configure remote logging write syslog entry networking section player registryobjectreferencehashingandstorageobjectsroregistrysectionmd

##### **Example**


registry createobjectroregistrysection networking
registrywritesyslog mysyslogserver
registryflush


specify syslog using either address hostname

developersdevelopersbrightscriptobjectreferencesystemobjectsmd
# System Objects



version older version

version

version

version

version

version

version

previous version


section describes object interact system software

rodevicecustomizationsystemobjectsrodevicecustomizationmd
rodeviceinfosystemobjectsrodeviceinfomd
roelectronsystemobjectsroelectronmd
roelectroneventsystemobjectsroelectroneventmd
roresourcemanagersystemobjectsroresourcemanagermd
rosystemlogsystemobjectsrosystemlogmd

developersdevelopersbrightscriptobjectreferencemd
# Object Reference



version older version

version

version

version

version

version

version

previous version




table content

interface methodsinterfacesandmethods
exampleexample
classesclasses
exampleexample
object class name syntaxobjectandclassnamesyntax
zoneszones
event loopseventloops
exampleexample

brightsign player standardized library brightscript object expose functionality software development publish interacting brightsign hardware create brightscript object

page section provide definition object used brightscript brief description list interface member function interface provided object class brightscript object selfcontained page object grouped page closely related depend another functionality

sample object used frequently creating application brightscript



rovideomodeobjectreferencepresentationandwidgetobjectsrovideomodemd configures video output interacts display using cecedid
rorectangleobjectreferencepresentationandwidgetobjectsrorectanglemd used define zoneswidgets screen object passed many object define screen area including rovideoplayer roimageplayer roimagewidget rohtmlwidget roclockwidget rocanvaswidget
rovideoplayerobjectreferencepresentationandwidgetobjectsrovideoplayermd play video file stream hdmi input
roimageplayerobjectreferencepresentationandwidgetobjectsroimageplayermd display image
rohtmlwidgetobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd display local remote html content using chromium rendering engine
ronetworkconfigurationobjectreferencenetworkingobjectsronetworkconfigurationmd used configure ethernet wifi local network parameter
rodeviceinfoobjectreferencesystemobjectsrodeviceinfomd used retrieve wide array system information including model type device serial number firmware version

## Interfaces and Methods

every brightscript object consists interface interface consists method example rovideoplayer object several interface including ifmessageport interface ifmessageport method setport

abstract interface ifmessageport exposed implemented rocontrolport rovideoplayer object setport method called object send event supplied message port discussed event loop section

##### **Example**


createobjectromessageport
video createobjectrovideoplayer
gpio createobjectrocontrolport brightsign
gpiosetportp
videosetportp


syntax make shortcut provided language interface name optional unless needed resolve name conflict example following line code carry exact function


gpiosetportp
gpioifmessageportsetportp


brightscript object consist interface interface define method concept property variable object interface level must implemented method interface

## Classes

class name used create brightscript object example class name video playback instance rovideoplayer initialize video playback instance would code similar following

##### **Example**


video createobjectrovideoplayer


note video name follows syntax outlined next section

## Object and Class Name Syntax

class name following characteristic

must start alphabetic character

consist alphabetic character number underscore symbol

case sensitive

reasonable length


## Zones

brightsign zone feature divide screen rectangle play different content rectangle

depending brightsign model zone contain video image html content audio clock text 4kx42 xdx32 xdx30 model display video zone screen hdx22 hdx20 lsx22 model display multiple zone type screen text zone contain simple text string configured display feed tickertype display

firmware zone support enabled default zone enabled image layer video layer default default behavior modified using therovideomodesetgraphicszorder method

zone support disabled calling enablezonesupportfalse zone enabled image layer hidden whenever video played video layer hidden whenever image played

## Event Loops 

writing anything simple script event loop need created event loop typically following structure

wait event

process event

return step


event number occurrence button pressed timer triggered message received video finished playing back convention event scripting brightscript object follows work flow

object type romessageport created script

object send event support ifmessageportifsetmessageport interface instructed send event message port using setport method multiple message port event message port usually simpler create message port event sent port

script wait event using builtin wait statement ifmessageportwaitmessage method

multiple object instance assigned message port script determines instance event originated process script jump back wait statement


##### **Example**


listens message different port display image file requested message body
createobjectromessageport

udp1 createobjectrodatagramreceiver 3000
udp1setportmp
udp1setuserdataport 3000

udp2 createobjectrodatagramreceiver 5000
udp2setportmp
udp2setuserdataport 5000

createobjectrorectangle0 1920 1080
createobjectroimageplayer
imgsetrectangler

loop
event wait0
typeevent rodatagramevent
print image play command received eventgetuserdata
displayfilesd eventgetstring
endif
endif
goto loop


developersdevelopersbrightscriptmd
# BrightScript



version older version

version

version

version

version

version

version

previous version


brightscriptreferencemanualver9pdfattachmentsbrightscriptreferencemanualver9pdf

note
youre trouble viewing file make sure accessing site http

brightscript powerful scripting language building medium networked application brightsign player library lightweight brightscript object brightscript enables access player application programming interface user utilize player underlying component networking medium playback screen interactive interface interpreted language rather compiled brightscript optimized generating featurerich application efficient userfriendly

section divided category

language referencebrightscriptlanguagereferencemd
outline characteristic brightscript language syntax operator statement type core library

object referencebrightscriptobjectreferencemd
provides directory publicly available object interface method comprise brightscript


refer brightscriptjavascript migration guidedevelopersplayerapisbrightscriptjavascriptmigrationguidemd info mapping brightscript javascript apis

plugins parser info plugins parser

developersdevelopersbrightsignregistrykeysigmpbehaviormd
# IGMP Behavior

version 8084 player accept forceigmpversion registry entry networking section entry allows customization player response igmp network environment following value

default behavior player igmpv3 unless querier older version present case player fall back

player always igmpv1

player igmpv2 possible fall back older querier present

player igmpv3 fall back


### Example

simple example set value reboot player registry change brightscript roregistry javascript registrydevelopersplayerapisjavascriptapisregistrymd detail


registryclass requirebrightsignregistry
registry registryclass

writes registry forcing player always igmpv1
registrywritenetworkingforceigmpversion1then
functionconsolelogwrite successful


developersdeveloperscloudapispostmancollectionsmd
# Postman Collections

bsn20control20cloudpostmancollectionjsonattachmentsbsn20control20cloudpostmancollectionjson
bsncontrolcloudproductionpostmanenvironmentjsonattachmentsbsncontrolcloudproductionpostmanenvironmentjson

# Control Cloud Library

postman library control cloud allows quickly familiarize different apis process associated control cloud subscription follow step create personnetwork create player setup provision player network player setup

warning
collection sample endpoint call introduce user infrastructure
comprehensive document available endpoint please bsncloudcloudapisbsncloudmainapismd remote dwsdeveloperslocalandremotediagnosticwebserverapisremotedwsapismd bdeploy endpoint documentation complete list endpoint usage

## Prerequisites

client client secret provided brightsign

postman

control cloud library collection bsncontrolcloudproduction environment

brightsign player active internet connection


## Steps

import control cloud library collection bsncontrolcloudproduction environment postman

postman environment bsncontrolcloudproduction using dropdown menu right

select icon select edit edit following variable variable value postman script

screenshot 20240105 113043 ampngattachmentsscreenshot202024010520at2011304320ampng

partnerlogin email address bsncloud person credential

partneremail email address partner login

partnerfirstname first name

partnerlastname last name

networkname name bsncloud network create name must unique within bsncloud database change value later want create multiple network example different customer

clientid provided brightsign

clientsecret provided brightsign

playerserial serial number player provision bsncloud network

playermodel model number player example xd1034

devicename device name arbitrary

setupname player setup name arbitrary

useraccesstokenlifetime amount time full access token network remains valid default minute

userself post self select send register bsncloud call also return person credential autogenerated password postman store

verify email address

bsncloud send email email address take minute

select link email verify address

dont need follow additional step create network since step performed using apis

select token self call root library select send self auth token postman store

userself post selfnetworks select send create bsncloud network credential network owner

select token full call root control cloud library select send

server return full auth token stored postman give access network created

renew full access token repeat step default timeout token minute

select token device registration call root control cloud library select send

server return device registration auth token postman store

device registration token separate user token allows player provision certain network

bdeploy post setup select send post setup bdeploy server setup postman store

bdeploy post device select send device serial number associated device setup created previous step

power reboot player player reboot several time provisioning network

device device select send list player network

remote info select send player information

developersdeveloperscloudapisusingapiaccessandrefreshtokensmd
# Using API Access and Refresh Tokens

warning
bsncloud changing authorization server able support security feature requested customer access refresh token lifetime changing
access token minute lifetime
refresh token minute lifetime
session lifetime hour
must ensure application andor script correctly handling refreshing token find stop working correctly
customer notified advance change time check prepare application script

# Refresh token-based authentication workflow

access bsncloud apis required submit credential order obtain access refresh token access token temporary credential grant access protected resource refresh token used obtain access token current one expire

application script access token endpoint authorizes successfully granted access token refresh token access token passed request allow resource accessed

info
bsncloud token endpoint

period time access token lifetime making call fail error access token expired point code refresh token exchange access token done passing refresh token token endpoint verifies refresh token issue access refresh token response access token subsequent call

process continues either

refresh token expired

refresh token revoked

current session expired


point need reauthenticate credential

following flow diagram show flow

screenshot 20240802 85533 ampngattachmentsscreenshot202024080220at208553320ampng

client application authenticates bsncloud token endpoint providing credential

credential valid access token refresh token returned result

client application make call must pas access token

component validates access token allows access resource

step continue access token expires signal returning error response status code

access token expires client application request access token providing refresh token

bsncloud token endpoint issue access token refresh token

step repeat refresh token expires revoked current session end

client need reauthenticate authentication server flow repeat step


info
bsncloud authentication documentationcloudapisbsncloudmainapismainrest
person authentication main rest http version 202206 authenticating person
person token refresh main rest http version 202206 person oauth2 token renewal
user authentication main rest http version 202206 authenticating user
user token refresh main rest http version 202206 user oauth2 token renewal

# Refresh Tokens

need access token refresh token dont long expiration date like month year access token someone manages hold access token long period even change password

idea refresh token make access token shortlived even compromised attacker get access short period refresh tokenbased flow authentication server issue onetime refresh token along access token application store refresh token safely

every time application sends request server sends access token authorization header server identify application using access token expires server send token expired response application receives token expired response must send refresh token obtain access token refresh token

something go wrong refresh token revoked mean application try access token request rejected enter credential authenticate

cant step constantly instead deal refresh token issuing many active access token efficient process lead increase storage decrease performance backend server permitted approach going forward adding limitation number unexpired access token application time

developersdeveloperscloudapismd
# Cloud APIs

brightsign cloud apis categorized follows

basic authorization apis control access bsncloud brightsignnetworkcom resource network

bdeploy provisioning apis provide tool managing automated deployment package

bsncloud service apis expose functionality brightauthor brightauthorconnected content management system monitor manage brightsign player


note diagram describe bsncloud server apis brightsignnetworkcom server apis work

## Basic Authorization APIs

accessapispngattachmentsaccessapispng

oauthcloudapisbsncloudmainapismainrest bearer token give user authorization communicate apis send request bdeploy remote apis

person oauth2 accessrefresh token return list network authenticated user send user oauth2 accessrefresh token correct network allows access network within scope allowed

return either valid token give access version bsncloud apis valid token give access version brightsignnetworkcom apis

bsncloud brightsignnetworkcom base url






## B-Deploy (Provisioning) APIs

setupapispngattachmentssetupapispng

bdeploy apis available bsncloud automated deployment player field apis deliver setup player allow creation modification setup package consist provisioning server provisioning setup server apis

provisioning server return given serial number bsncloud connected device provides rest apis

provisioning setup server store serf setup package presentation package firmware update provides addition rest apis make call retrieve serial number url


## BSN.cloud and .com Service APIs

serviceapis copypngattachmentsserviceapis20copypng

apis expose functionality brightauthor brightauthorconnected content management system using standard endpoint entity method developer apis build custom content management interface feature developed content management system apis also used devicefleet management

bsncloud apiscloudapisbsncloudmainapismd allow user cloudbased infrastructure interact networked brightsign player partner bsncloud apis without server

brightsignnetworkcom apiscloudapisbsncommainapismd older brightsign network interact brightsign player

developersdevelopershtmldevelopmentdisplayinghtmlwithbrightauthormd
# Displaying HTML with BrightAuthor



table content

html guidelineshtmlguidelines
zoneszones
zorderingzordering
content sourcingcontentsourcing
using custom fontsusingcustomfonts
exporting html5 presentationexportinganhtml5presentation
caching storagecachingandstorage
using html portrait orientationusinghtmlwithportraitorientation
integrating touchscreen contentintegratingtouchscreencontent
disguising network latencydisguisingnetworklatency
displaying scrollbarsdisplayingscrollbars

section cover integrate html page brightauthor presentation html page presentation click medium library select html5 state drag playlist area prompted local html file remote page presentation

# HTML Guidelines

following general rule using html content brightauthor

## Zones

multiple zone containing html content brightauthor presentation

html content inserted video image zone image zone cannot html content video zone

dimension html backgroundpage must match size zone brightauthor cannot background image scaling zone different size


attachmentsba35201png

## Z-Ordering

html content show highest zlevel graphic zone meaning html zone cover zone contain image text behavior extend touch screen integrating touchscreen content detail

html content placed front behind zone containing video content depending graphic plane position setting zone containing html content configurable edit layout

html page contains video enable native video plane playback option enabled html5 state html page always display video zone


## Content Sourcing

html content originate remote server local server local storage card player presentation containing html content also downloaded onto local storage brightsign network

html content relies asset multiple location make sure check enable external data creating editing html5 state


## Using Custom Fonts

creating html5 state brightauthor click font button custom true type font file html page feature work local remote html content

presentation published font file though located file directory indexhtml file accessed standard fontfamily attribute htmlcss


## Exporting an HTML5 Presentation

exporting presentation contains multiple html page also export full asset folder associated page page share common asset folder entire content duplicated multiple time become problematic asset folder contain large content file need prune andor rearrange asset folder duplicated export


# Caching and Storage

brightauthor allows configure common browser caching storage function player enable function open brightauthor html presentation navigate edit preference storage check limit storage space function allocate space following function

html data amount space dedicated html application cache

html local storage amount space dedicated javascript variable data


select specify absolute size possible specify combined segment larger smaller absolute size storage device select specify percentage need ensure percentage equivalent absolute size local storage player

note
html local storage feature available brightauthor version 41112 later similar feature available file presentation property html section earlier version

# Using HTML with Portrait Orientation

follow step create digitalsignage canvas portrait oriented

warning
instruction apply brightauthor version 430x later

edit aspect ratio authoring software dreamweaver reverse monitortelevision resolution example plan displaying portrait content 1080p resolution 1080x1920 rather 1920x1080

create presentation player brightauthor

monitor orientation portrait click create

prompted select template choose full screen

html content playlist


attachmentsba352046png

# Integrating Touchscreen Content

enable touchscreen event html page checking enable mouse touch event creating html5 state html5 state description detail

note
brightsign player compatible touchscreen standard driver note manufacturer claim support still custom driver discussion list touchscreen model tested brightsign player

note touch event received html page brightauthor rectangular touch event therefore zone html page overlapping zone containing rectangular touch event touching area overlap send event zone time case even zone completely cover visually depending type action triggered zone touchevent overlap cause crashing issue presentation stability unless certain consequence make sure zone touchenabled html content zone rectangular touch event overlap

warning
creating overlap shown unintended consequence

attachmentsba35207png

# Disguising Network Latency

brightsign player load html content delay based network latency preload image sidestep issue note solution necessary html asset located local storage player

drag drop image file medium library

check initial state editing image state

timeout event image

specify timeout three second desired

timeout event transition html5 state


attachmentsba35203png

# Displaying Scrollbars

browser scrollbars disabled default brightauthor display scrollbars reference simple file html page

forcescrollbarscssattachmentsforcescrollbarscss

developersdevelopershtmldevelopmentdisplayinghtmlwithbrightauthorconnectedmd
# Displaying HTML with BrightAuthor:connected



table content

html guidelineshtmlguidelines
zoneszones
zorderingzordering
content sourcingcontentsourcing
using custom fontsusingcustomfonts
exporting html5 presentationexportinganhtml5presentation
chromium video playbackchromiumvideoplayback
caching storagecachingandstorage
using html portrait orientationusinghtmlwithportraitorientation
integrating touchscreen contentintegratingtouchscreencontent
disguising network latencydisguisingnetworklatency
displaying scrollbarsdisplayingscrollbars

page cover integrate html page brightauthorconnected presentation html page presentation select html5 widget bottom content window drag content panel page describes widget

## HTML Guidelines

### Zones

multiple zone containing html content brightauthorconnected presentation

html content inserted video image zone image zone


### Z-Ordering

html content show highest zlevel graphic zone meaning html zone cover zone contain image text behavior extend touch screen

html content placed front behind zone containing video content drag graphic zone video zone zone menu zone property panel image

html page contains video enable native video playback option enabled html5 state html page always display video zone


attachmentsscreenshot202023090720at2010474220ampng

### Content Sourcing

html content originate remote server local server local storage card player presentation containing html content also downloaded onto local storage brightsign network

### Using Custom Fonts

custom font specify font script font file directory file used brightauthorconnected

### Exporting an HTML5 Presentation

exporting presentation contains multiple html page also export full asset folder associated page page share common asset folder entire content duplicated multiple time become problematic asset folder contain large content file need prune andor rearrange asset folder duplicated export

### Chromium Video Playback

html5 widget enable native chromium video playback option version 1192 later brightauthorconnected feature available player explained page

note
partner using custom html playback option series playershtmldevelopmenthtmlplaybackoptionsonseries5playersmd guidance setting option

## Caching and Storage

brightauthorconnected allows configure common browser caching storage function player enable function brightauthorconnected presentation select enable limit storage admin application preference allocate space wish select apply allocate space following function

html data amount space dedicated html application cache

html local storage amount space dedicated javascript variable data

html indexed amount space dedicated indexeddb content


attachmentshtmllimitoptionspng

## Using HTML with Portrait Orientation

create digitalsignage canvas portrait oriented simply create portrait presentation insert html5 widget

## Integrating Touchscreen Content

enable touchscreen event html page checking enable mouse touch event creating html5 state

## Disguising Network Latency

brightsign player load html content delay based network latency preload image sidestep issue note solution necessary html asset located local storage player

brightauthorconnected interactive

drag drop image file main panel

initial state editing image state

specify timeout three second desired timeout event

timeout event transition html5 state


## Displaying Scrollbars

browser scrollbars disabled default brightauthorconnected display scrollbars reference simple file html page

forcescrollbarscssattachmentsforcescrollbarscss

developersdevelopershtmldevelopmentdisplayinghtmlwithoutbrightauthormd
# Displaying HTML without BrightAuthor



table content

simple webpage scriptsimplewebpagescript
portrait orientationportraitorientation
displaying scrollbarsdisplayingscrollbars
mobile scrollbarsmobilescrollbars

method display html without brightauthor

play html page local storage without autorun script placing indexhtml file along file folder containing page content root folder player storage

brightscript display local remote html content section pertain using rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd brightscript object display html learn brightscript brightscriptdevelopersbrightscriptmd section


## Simple Webpage Script

simple script outlined display webpage stored remote server save script autorunbrs file place card publish player

want display webpage located local storage replace line filename html file filemytestpagehtml

notice script sleep10000 line line delay loading urlthis necessary compensate connection delay occur network dont script brightsign player connect time load page resulting cannot resolve host error indicates player internet connection certain network configuration especially player utilizes dhcp need increase sleep amount millisecond give player time establish connection loading page

parameter rohtmlwidget defined associative array passed object creation rohtmlwidget pagedevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd information creating configuring html widget


main
msgport createobjectromessageport
createobjectrorectangle 1920 1080

config


createobjectrohtmlwidget config
hsetportmsgport
sleep10000
hshow
true
wait0 msgport
print typemsgtypemsg
typemsg rohtmlwidgetevent
eventdata msggetdata
typeeventdata roassociativearray typeeventdatareason rostring
print reason eventdatareason
eventdatareason loaderror
print message eventdatamessage
endif
endif
endif




## Portrait Orientation

rotate content html page include transform parameter creating rohtmlwidget object clockwise portrait orientation transformrot90 counterclockwise portrait orientation transformrot270 youre using simple webpage script parameter config associative array line

## Displaying Scrollbars

browser scrollbars disabled default enabled including scrollbarenabledtrue parameter creating rohtmlwidget object youre using simple webpage script scrollbarenabledtrue config associative array line

also enable scrollbars using example referencing simple file

forcescrollbarscssattachmentsforcescrollbarscss

## Mobile Scrollbars

browser scrollbars default desktop style prominent visible time configure chromium instance mobilestyle scrollbars less prominent visible scrolling writing overlayscrollbar entry html section registry


htmlregistry createobjectroregistrysection html
htmlregistrywriteoverlayscrollbar


developersdevelopershtmldevelopmenthtmlauthoringresourcesmd
# HTML Authoring Resources

large number online resourcesincluding tutorial sample template widgetsavailable help started creating content html5 html5 standard offer huge advantage developer including digital signage author following website great place learn create page using html5






## WordPress 

wordpress excellent html5 resource provides intuitive approach creating digital signage benefit using wordpress architecture

wordpress offer advanced html5 support premade widget ranging weather ecommerce system also support advanced html5 option using css3 feature site also provides html5 widget

either wordpress website install wordpress instance server

wordpress ecosystem template creator offer sophisticated template wide range industry template creator include following








## HTML5 Authoring

common html5 authoring application

adobe tool dreamweaver illustrator indesign photoshop

aptana studio

coffeecup software

developersdevelopershtmldevelopmenthtmlbestpracticeshtmlcachingmd
# HTML Caching

page cover caching technique display html content brightsign player offer novel solution brightauthor brightscript well support common nodejs javascript caching solution

## Storage and Memory

discussing html caching technique important understand storage memory limitation player brightsign player html content chromium engine default chromium reserve plus total size player storage device memory player also limited memory html graphic javascript amount varies player model consult list detail

change storage value brightauthor

navigate edit preference storage

check limit storage space function

space allocated html graphic javascript make sure

using specify absolute size specified segment neither larger smaller absolute size storage device

using specify percentage percentage must


limitation shared across rohtmlwidget instance rohtmlwidget brightscript object handle html process

## Caching Capabilities

brightsign player offer flexible toolset caching html content section discus novel brightsign solution enable common method nodejs javascript

### BrightSign solutions

brightsign player offer html caching solution

local storage card player store html content playback method eliminates connectivity latency issue arise networked solution must done player player basis make local storage unattractive dealing large fleet device

assetpool brightscript object assetpool sharded hash directory recommended large file count application assetpool filled assetfetcher object acquire content online store later playback either sha1 besha1 hash protocol consult page information assetpool


### Node.js and JavaScript solutions

brightsign player also support nodejs javascript caching technique nodejs

using brightauthor nodejs must first enabled brightscript rohtmlwidget object

using brightauthorconnected nodejs initialized presentation state property user interface


nodejs running player user javascript caching method cache content recommended content acquisition method xmlhttprequest fetch service worker keep memory limitation mind example xmlhttprequest cause player model crash used download file larger 100200mb xmlhttprequests storage reservation exceed memory limitation recommend using fetch

cannot service worker cache video content brightsign player medium player infrastructure later video playback chromium network brightsign recommends indexeddb storage cache content playback according instruction

htmljavascript test download example

note
html widget cannot cache video listed appcache manifest difference chrome desktop brightsign device video playback architecture please service worker indexeddb cache content instead appcache deprecated

### Using Blobs

brightsign video player play blob url referring item indexeddb html5 filesystem however cannot play blob url referring javascript object memory

videobrowserstoragehtml example

indexdbplaybackexamplezipattachmentsindexdbplaybackexamplezip

developersdevelopershtmldevelopmenthtmlbestpracticesmd
# HTML Best Practices



table content

content restrictionscontentrestrictions
browsingwebbrowsing
flash contentflashcontent
videovideo
graphics4kgraphics
xtx44 xtx43xtx44xtx43
xdx34 xdx33 hdx24 hdx23 ls424 ls423 4kx42xdx34xdx33hdx24hdx23ls424ls4234kx42
pixel size coordinate modespixelsizesandcoordinateswith4kmodes
image sizesimagesizes
memory performancememoryandperformance
fontswebfonts
creating html pagescreatinghtmlpages
brightsign extensionsbrightsignextensions
rasterizationgpurasterization
optimized image renderingoptimizedimagerendering
renderer version supportrendererversionsandsupport
animation addon librariesanimationsandaddonlibraries
javascript animationsjavascriptanimations
webglwebgl
vector animationsvectoranimations
canvas animationscanvasanimations
push technologypushtechnology
file storagefilestorage
file downloadsfiledownloads
transformscsstransforms
html storagehtmlstorage
initializationinitialization
storage pathstoragepath
storage quotastoragequota
touchscreen supporttouchscreensupport
debugging webpagesdebuggingwebpages
inspectorwebinspector
enabling inspectorenablingthewebinspector
inspecting webpageinspectingawebpage
chromium version compatibilitychromiumversioncompatibility
trace eventstraceevents
creating traceevent directorycreatingatraceeventdirectory
enabling traceevent systemenablingthetraceeventsystem
example javascriptexamplejavascript
viewing trace eventsviewingtraceevents
additional documentationadditionaldocumentation
disabling staged featuresdisablingstagedes6features

page cover content requirement ability restriction html rendering engine brightsign player

## Content Restrictions

following content restriction associated html page

### Web Browsing

brightsign player intended generalpurpose browser best think brightsign unit html player interactive capability websurfing tool page thoroughly tested used digital signage

### Flash Content

brightsign player support flash content html page embedded flash content display correctly flash authoring application including adobe creative suite tool allow export flash content html

### Video

html videohtmldevelopmenthtmlvideomd page usage rule regarding html video

### 4K Graphics

many brightsign model output video mode 3840x2160 model render html

#### XTx44, XTx43

xtx44 xtx43 model support native html graphic plane page detail note following performance restriction using native html graphic

animation exceed intensive animation exhibit framerates

nonhwz video likewise limited hwzhtmldevelopmenthtmlvideomd enabled video element native

recommend displaying image time example slideshow image displayed next image preloaded image exceed 3840x2160 size

recommend using swap memorydevelopersbrightscriptobjectreferencehashingandstorageobjectsrovirtualmemorymd possible

page many layer memory native enabling gfxmemlargedevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideomodemd setting help mitigate issue


#### XDx34, XDx33, HDx24, HDx23, LS424, LS423, 4Kx42

model support graphic 1920x1200 page detail upscaled video mode page must specified 1920x1080 2048x1080 upscaled

### Pixel Sizes and Coordinates with 4K Modes

noted webpage often upscaled outputting video mode relative property value scale automatically pixel value need modified account difference video graphic heredevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrorectanglemd information using coordinate upscaled video mode

### Image Sizes

image larger 2048x1280x32bpp 3840x2160x32bpp xtx34 xdx33 player displayed default video mode used player upscale image resolution accordingly though native graphic enabled xtx43 default limit increased brightscript using rovideomodesetimagesizethreshold method

without altering default maximum resolution increase maximum width image sacrificing height using 3840x640x32bpp image non4k player allowed also increase maximum widthheight reducing value using 3840x2160x16bpp non4k player allowed

note
performance reason recommend downscaling image consumes considerably resource either displaying image native size upscaling

### Memory and Performance

amount memory available html application varies model player series

series player

unlike series older player series player dont preallocated graphic system memory limitation memory chromium demanding application dont deplete memory

series older player

xtx43 xtx44 512mb graphic 512mb javascript

xdx33 xdx34 256mb graphic 512mb javascript

hdx23ls423ho523 256mb graphic 128mb javascript


note

memory available graphic reduced number factor including number layer complexity animation webgl

javascript memory subject hard limit javascript memory garbage collection chromium terminate active process

html widget javascript heap possible overcommit javascript memory multiple html widget active



often best improve graphic performance ensure image scaled desired output resolution rendered html

note
chromium inspector determine amount resource used webpage

### Web Fonts

font file included referenced html page text rendered using default system font functional default font little aesthetic appeal recommend including font file digitalsignage application supported font type include truetype font file opentype font open font file woff woff2

## Creating HTML Pages

follow step creating html page

make sure html page aspect ratio signage display using html content brightauthor zone smaller screen page aspect ratio zone

master aligned building html page ensure correct alignment

creating html site make sure webpage asset image file video file contained within folder local disk folder site folder meaning asset folder subfolders used production webpage asset folder display project published

test layout appearance page locally opening google chrome similar rendering capability brightsign player

want publish resourceintensive presentation video element multiple transforms using html recommend using class 10mbs card


## BrightSign Extensions

brightsign implementation chromium engine includes several platformspecific extension extension video element covered html videohtmldevelopmenthtmlvideomd page

### GPU Rasterization

rasterization enabled default firmware version later

### Optimized Image Rendering

imagerendering property assigned optimizespeedbs value using value ensures chromium us lowerquality faster bilinear filtering scaling image less recommend using value page scale image runtime

## Renderer Versions and Support

following table describes version webrendering engine used version brightsign firmware

rendering engine version brightsign version

chromium
chromium
chromium
chromium
chromium
webkit

page download listed chromium version page determine specific function call extension supported corresponding version chrome

note
chromium version later refuse sha1 certificate page information

## Animations and Add-on Libraries

section outline support animation addon library chromium engine brightsign player


limit file directory depth prevent issue caused overly complex folder structure

### JavaScript Animations

animation javascript timer including jquery animate library make efficient resource accurate enough achieve smooth animation reason recommend using animation whenever possible jquery transit library us animation provides similar animate library

note
best result animating image recommend using image original size instead scaling first example 480x270 icon rotate smoothly image originally 480x270 rather scaling 1280x720 image attempting rotate

### WebGL

brightsign player support opengl javascript webgl

note
texture sometimes fail load webgl exceed maximum allowed image size brightsign player case rovideomodesetimagesizethresholddevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideomodemd brightscript method increase maximum size texture

### Vector Animations

protocol used specify vector animation

### Canvas Animations

bitmap animation display smoothly less 1080p html canvas setting canvas size 720p allows larger highquality animation occupy screen

### Push Technology

long polling technique tested proven work brightsign player

websocket protocol fully supported nodejshtmldevelopmentnodejsmd implementation brightsign chromium instance production environment recommend using http initiate websocket connection server using connection rather connection

example websocket application available brightsign github page

### File Storage

brightsign player support several file storageindexing technology including indexeddb html filesystem javascript storage class location size storage database initialization rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd

### File Downloads

youre using javascript download file reccomend using fetch nodejs file system module perform downloads pagehtmldevelopmentnodejsmd detail

### CSS Transforms

transforms specified webkit transforms performing transform graphic element specify transform inline

following code show example effective transform brightsign player

example


style

flipme
webkitanimationnameflipon
webkitanimationfillmodeforwards
webkitanimationiterationcount1
webkitanimationduration2s



webkitkeyframes flipon

webkittransformrotatey0deg
webkittransformrotatey90deg
webkittransform rotatey360deg


style


## HTML Storage

following rohtmlwidget method used configure html storage brightsign player

setlocalstoragedir

setlocalstoragequota

setwebdatabasedir

setwebstoragequota

setappcachedir

setappcachequota


note
behavior rohtmlwidget storage method changed behavior described updating player earlier cause stored html data player reset

### Initialization

method take effect rohtmlwidget instance created dont apply rohtmlwidget instance called case storagepath storagequota initialization parameter

### Storage Path

setlocalstoragedir setwebdatabasedir setappcachedir method configure storage path calling method overwrite storage path configured method

without storage path example using incognito browser nothing persist finished chromium instance want data persist reboot widget creation must storage path nonpersistent incognito mode used total system memory reserved browser storage memory shared multiple rohtmlwidget instance

### Storage Quota

setlocalstoragequota setwebstoragequota setappcachequota method configure storage quota applies persistent html storage player storage path specified without storage quota chromium default reserving plus total size storage device

multiple rohtmlwidget instance configured default quota shared among

## Touchscreen Support

brightsign player compatible touchscreen standard driver note manufacturer claim support still custom driver discussion list touchscreen model tested brightsign player

## Debugging Webpages

### Web Inspector

inspector debug webpage local network

note
javascript console used nonproduction presentation disabled publish production environment us memory lead frequent reboots compromise security

#### Enabling the Web Inspector

inspector enabled using brightauthorconnected brightauthor brightscript

brightauthorconnected select allow javascript console chromium debugging section enable javascript console presentation state property option disable chromium debugging uncheck either box

brightauthor brightauthor presentation navigate file presentation property html check enable javascript console note 8531 need also enablewebinspector registry html section enable javascript console inspectorserver rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd information

brightscript creating rohtmlwidget instance include inspectorserverdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd initialization parameter specify port number note 8531 must enablewebinspector registry enable inspector chromium player nothing inspector disabled example



createobjectroregistrysectionhtml
regwriteenablewebinspector
regflush


want change inspector port must edit configuration rohtmlwidget inspectorserver rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd information

note
enabling inspector creates security vulnerability brightsign player page detail

#### Inspecting a Webpage

html content running brightsign player follow step inspect

open chrome desktop computer connected local network

enter following address chromeinspectdevices

device section click configure

enter player address inspector port field image page brightsign player displayed bottom page

dont know player address power player microsd card storage device removed moment address displayed screen

enabled inspector brightauthor port 2999

click inspect button next page debugging session launched window unlike local page page content displayed left pane inspector window right used debug page


attachmentsinspectorpng

note
adding device list cause performance issue especially device online chrome client continue search offline device

#### Chromium Version Compatibility

brightsign player older version chromium recent desktop version newer desktop chrome release work inspector youre trouble using inspector version chrome download install version

linux



window 64bit


note
youre using inspector manually step javascript code encountering uncaught error debugger cause player crash known inspector

larger collection supported chromium downloads found

### Trace Events

chromium traceevent system allows debug javascript memory leak performance issue rendering problem feature available firmware version 7082 later unlike tracedebugger browser content brightsign player write json trace file local storage import chrome

trace event enabled brightsign player chromium capture trace message circular buffer player take regular snapshot buffer writes root directory microsd card json file

note
traceevent system easily generate gigabyte data local storage recommend disabling production environment

note
stackoverflow page information memory leak using consolelog complex object

#### Creating a TraceEvent Directory

enabling traceevent system create directory named brightsignwebinspector root directory microsd card player directory missing player record trace event enabled registry conversely disable trace event deleting brightsignwebinspector directory storage device

#### Enabling the TraceEvent System

traceevent system enabled configured writing brightsign player registry brightscriptdevelopersbrightscriptobjectreferencehashingandstorageobjectsroregistrymd javascriptdevelopersplayerapisjavascriptapisregistrymd enable traceevent system write following key html section registry

string tracecategories commaseparated list trace event category enable category name documented link

tracemaxsnapshots maximum number jsontrace snapshot file brightsignwebinspector directory limit reached counter wrap around begin writing oldest trace file

tracemonitorinterval frequency second player take snapshot traceevent buffer recommend second default value


##### Example (JavaScript):


registryclass requirebrightsignregistry
registry registryclass
registrywritehtml
tracecategories toplevelblinkgcdisabledbydefaultmemoryinfradisabledbydefaultblinkgcdisabledbydefaultskiagpucache
tracemaxsnapshots
tracemonitorinterval

function
consolelogwrite successful



#### Viewing Trace Events

follow step view trace event

transfer json trace file brightsignwebinspector directory

open chrometracing chromium instance

import json trace file


merge multiple trace file however long trace capture many trace event view youll likely need write script process

#### Additional Documentation

following link explanation trace event








## Disabling Staged ES6 Features

feature finalized still contain bug chromium version used brightsign crash occur javascript application framework code used build application us feature example known issue chromium version cause crash brightsign xtx44 xdx34 player

bypass issue disable staged experimental feature using disablejavascriptharmonyshipping registry flag requires firmware version 7149 later following example show registry flag using registrydevelopersplayerapisjavascriptapisregistrymd javascript module also roregistrydevelopersbrightscriptobjectreferencehashingandstorageobjectsroregistrymd brightscript object


registryclass requirebrightsignregistry
registry registryclass


systemclass requirebrightsignsystem
system systemclass


registrywritehtml jsdisableharmonyshipping1then
functionconsolelogwrite successful


systemreboot


enabling registry flag limit available javascript syntax however feature available application must written compatible enabling flag cause syntax error similar issue

developersdevelopershtmldevelopmenthtmlplaybackoptionsonseries5playersmd
# HTML Playback Options on Series 5 Players

way playback html audio video series player

series older player video decode handed default brightsign application deal decode display


series player option registry value enable builtin chromium video player resulting chromium play back video similarly desktop chromium series player automatically hardwareaccelerated decode chromium video player enabled option available series earlier player regardless version


brightsign video audio feature provided brightsign video player chose chrome brightsign html videohtmldevelopmenthtmlvideomd feature supported like running chrome browser chromium much poorer streaming support application fewer hardware accelerated video decode level profile supported

customer want take advantage unique capability native chrome

switch brightsign video player chrome medium player


registrysection createobjectroregistrysection html
registrysectionwriteusebrightsignmediaplayer switch chromium medium playback


switch chrome medium player brightsign video player


registrysection createobjectroregistrysection html
registrysectiondeleteusebrightsignmediaplayer switch back default brightsign medium playback





registrysection createobjectroregistrysection html
registrysectionwriteusebrightsignmediaplayer switch back brightsign medium playback


developersdevelopershtmldevelopmenthtmlvideomd
# HTML Video



table content

streaming videostreamingvideo
streaming parametersstreamingparameters
youtubeyoutube
medium source extensionsmediasourceextensions
live streaminghlslivestreaming
hdmi inputhdmiinput
multiple video elementsmultiplevideoelements
small videossmallvideos
view modeviewmode
videohwzvideo
zordering videozorderinghwzvideo
transforming videotransforminghwzvideo
fading video streamsfadinghwzvideostreams
video transparency extensionshwzvideotransparencyextensions
video decoder selected playbackhowvideodecodersareselectedforplayback
video decryptionvideodecryption
video stream parsingvideostreamparsing
video streamsvideostreams
audio streamsaudiostreams
subtitle caption streamssubtitleandcaptionstreams
pattern matching behaviorpatternmatchingbehavior
examplesfurtherexamples
video track switchingvideotrackswitching
audio routing audiovideo elementsaudioroutingaudiovideoelements
html video timecode playbackhtmlvideotimecodeplayback
chroma keyingchromakeying

note
documentation applies firmware version later

video element play streaming video rtsp local video file also display hdmi input xd1230 xd1132 4k1142 xt1143 input xd1230

## Streaming Video

streaming video playback achieved using standard html video element appropriate attribute scheme used playback







rtsp


note pauseresume command currently work stream

### Streaming Parameters

configure streaming video using number unique brightsign attribute attribute overridden parameter included streaming

example html


video srcudp239192115004 xbsstreamtimeout0


example javascript


videoplayersetattributexbsstreamlowlatency


following streaming parameter supported

xbsstreamtimeout length time millisecond wait stream start abandoning playback passing zero indicates video player wait indefinitely default timeout value 5000ms http stream 3000ms stream

xbsstreamlatency amount deviation millisecond default latency value example value reduce latency half second value increase latency half second value specify default latency specifying negative value change buffer size instead give buffer less time fill playback begin usable value extend approximately though value differ depending network environment reducing latency much result obvious playback stutter

xbsstreamfadein fadein length millisecond stream default nonhttp stream fade value 1500ms contain video 4000ms contain audio http stream default fade value

boolean xbsstreamlowlatency lowlatency mode rtsp stream setting parameter true achieve lowest possible latency stream reduced maximum bitratewhich often useful camera stream parameter false default

xbsintrinsicwidth intrinsic width source video

xbsintrinsicheight intrinsic height source video


#### Achieving Low Latency

three option reduce latency series brightsign player

##### x-bs-stream-latency

xbsstreamlatency flag buffer described streaming parameter example latency reduced half second millisecond


video srcudp239192115004 xbsstreamlatency500


##### x-bs-no-force-capture

xbsnoforcecapture flag true video capture bypass framerate conversion introduce following limitation

transform value identity work

screenshots correct

encoded video frame rate video mode output must match


example


video srcudp239192115004 xbsnoforcecapture1


##### x-bs-no-reordering

xbsnoreordering flag improve latency disable playback bslices example


video srcudp239192115004 xbsnoreordering1


page information modifying latency audio video stream

#### Native Chrome Media Player

series player support selecting native chrome video playback hardware acceleration using default brightsign medium player video playback pick option best case html playback option series playershtmldevelopmenthtmlplaybackoptionsonseries5playersmd

##### WebRTC

webrtc brightsign always us native chrome video playback

series player running 90115 later automatically hardwareaccelerated decode case

series older player support hardwareaccelerated decode native chrome video playback decode done software recommend trying approach player

#### Intrinsic Video Size

following order precedence used determine intrinsic size video

xbsintrinsicwidth xbsintrinsicheight attribute

size image specified poster attribute

width height attribute video element

size reported webmediaplayer

default size defined 300x150


width height attribute video element specified rendering engine assumes intrinsic size source video video element size scale video fill video element ignoring aspect ratio source video necessary additionally width height attribute video specified size available source example stream still loading video initially default resolution 300x150

know size aspect ratio source video beforehand xbsintrinsicwidthxbsintrinsicheight attribute ensure aspect ratio source video maintained scaled video element example video window oriented portrait width1080 height1920 specifying intrinsic width height 1920x1080 ensures landscape video scale maintaining aspect ratio letterboxing appropriately likewise video scale intrinsic widthheight immediately video element lack width height parameter rather possibly defaulting 300x150 short time

### YouTube

brightsign player support youtube video playlist

### Media Source Extensions

medium source extension enabled automatically series player however still disabled setting msesupport flag registry

support available series must specifically enabled enter following code brightsign prompt


registry write html msesupport


### HLS Live Streaming

brightsign player support live streaming large playlist usually result server delivering playlist rather live playlist cause performance issue

## HDMI Input

must input video source using following tvbrightsignbizhdmi note cannot substitute another host brightsignbiz

example


video width320 height240
source srctvbrightsignbizhdmi
video


## Multiple Video Elements

default player support maximum active video element time hdl model support amount video element page long additional video element attribute empty string modifying string enable disable video element page

enable mosiac mode using setdecodermodedevelopersplayerapisbrightscriptjavascriptobjectsbsvideomodemd javascript method increase minimum allowed number video element

## Small Videos

brightsign player support video less pixel width height however video scaled beyond limit making video element smaller 64x64 desired downscaling behavior ensure video element viewmodescaletofillandcrop attribute

## View Mode

firmware version later video scale aspect ratio video element scaletofill earlier version firmware video element maintain aspect ratio source video scaletofit default behavior modified using viewmode attribute however recommend using standard method objectfit modify view mode behavior video element

viewmodescaletofill scale video fill window aspect ratio source video ignored video appear stretched

viewmodescaletofit letterboxes video

viewmodescaletofillandcrop scale video fill window aspect ratio source video maintained video cropped


## HWZ Video

html video element optional attribute disabled default disabled video frame decoded dedicated hardware routed display enabled video frame instead routed directly hardware compositor bypassing choice whether enable depends application single obviously right answer consideration

limited 8bit color depth 10bit video must routed hardware video plane order retain full color depth

case limited fullhd resolution video must routed hardware video plane avoid loss resolution even platform configured support graphic unlikely achieve high enough frame rate fullmotion video playback

hardware video compositor perform simple scaling alphablending support arbitrary transforms video complex styling must routed order display correctly likewise video need captured canvas webgl processing must routed recommend testing manipulated video thoroughly using production environment

video routed graphic repaint required every frame consumes large amount system bandwidth result stuttery playback able keep required frame rate time


general recommend routing video hardware compositor unless specific need processing application routing video hardware compositor achieved setting hwzzindex1 video element question cause compositor stack video graphic layer according zindex property

also enable video html widget using following method

brightauthorconnected select enable native video playback html5 state

brightauthor check enable native video plane playback html5 state

brightscript call sethwzdefaulton rohtmlwidget instance


### Z-Ordering HWZ Video

video element routed hardware compositor given hwzzindex2 lower negative zindex stacked behind note specific instance stacking order overridden alternatively possible pas positive zindex value attribute done video element stacked front graphic layer overriding stacking order higher positive value zindex front

route video playback pas hwzoff hwzzindex0 equivalent legacy value hwzon equivalent hwzzindex1 avoided

zindex property layer element without enabling layer order shown text video middle image back


body stylebackgroundcolorblue
stylepositionabsolutecolorredfontsize100pxzindex1 hello brightsign
srcposterpng stylepositionabsoluteleft0pxtop0pxwidth800pxheight800pxzindex3img
video srccoffee2mp4 stylepositionabsoluteleft0pxtop0pxwidth480pxheight320pxzindex autoplay loop mutedvideo
body


enabled zindex property stylezindex1 overridden zindex value attribute maintain correct zordering position element


body stylebackgroundcolorblue
stylepositionabsolutezindex1color redfontsize 100px hwzzindex1 hello world
srcposterpng stylepositionabsoluteleft0pxtop0pxwidth800pxheight800pxzindex3 hwzzindex3img
video srccoffee2mp4 stylepositionabsoluteleft0pxtop0pxwidth480pxheight320pxzindex hwzzindex2 autoplay loop mutedvideo
body


### Transforming HWZ Video

optional transform parameter attribute rotate mirror video element zindex parameter must also specified transform work transform parameter assigned following value

identity transformation default behavior

rot90 degree clockwise rotation

rot180 degree rotation

rot270 degree clockwise rotation

mirror horizontal mirror transformation

mirrorrot90 mirrored degree clockwise rotation

mirrorrot180 mirrored degree clockwise rotation

mirrorrot270 mirrored degree clockwise rotation


note
multiple video extension separated semicolon semicolon also appended final parameter

example


video rotated degree behind graphic layer
video srcexamplemoviemp4 hwzzindex1 transformrot180


### Fading HWZ Video Streams

fade parameter allows control fading behavior streaming video video element setting apply local video fade parameter allows control fading behavior decoded video video element setting apply hdmi affect audio operate independently streamfadein

fade parameter accepts following value

auto video player currently showing anything hasnt played anything previous loaded video cleared next video fade video player currently playing video paused stopped without cleared next video fade default behavior

always video end video window black video fade

never video transition without fade effect


### HWZ Video Transparency Extensions

enabled video element video window also support luma chroma key video transparency zindex parameter must also specified transparency work luma chroma key specified follows

lumakeyhexvalue

crkeyhexvalue

cbkeyhexvalue


example

example video video layer front graphic layer lumakeyed video


video srcexamplemoviemp4 hwzzindex1 lumakeyff0020


### How Video Decoders are Selected for Playback

system software selects video decoder based resolution probed video file standard mode attempt select decoder closest maximum supported resolution 1920x1080 decoder 3840x2160 decoder without exceeding maximum resolution decoder configured mosaic mode match video resolution specified timeslicemode instead decoder support maximum resolution select decoder matching zorder rovideoplayer instance using tofront toback method zorder decoder using rovideomodesetdecodermode method

also select decoder manually first configure decoder using rovideomodesetdecodermode method friendlyname specified calling method designate decoder video playback

select decoder brightscript pas associative array rovideoplayerplayfile method containing decoderfriendlyname parameter

playfilefilenametext1mov decodermainvideo

select decoder html video include decoderfriendlyname property attribute

video hwzdecodermainvideo video
video hwzdecodersdvideo video


maxusage decoder determines many video player assigned decoder using system software algorithm described abovevideo player beyond maxusage limit assigned another decoder displayed hand manually assign video player using friendlyname decoder assign video player decoder maxusage limit cause unpredictable videodisplay behavior

## Video Decryption

html video used decrypt video file stream streaming decryption currently supported protocol http protocol http paired mpeg2 transport stream using multicast mpeg2 transport stream elemental stream provide player

video support encryptionalgorithm encryptionkey method

encryptionalgorithm fileencryption algorithm following current option

aesctr algorithm mode

aesctrhmac algorithm mode hmac

tsaesecb algorithm mode harmonic prostream algorithm currently used streaming encryptiondecryption

tsaescbcrbt algorithm mode residual block termination algorithm used streaming encryptiondecryption

encryptionkey byte array consisting bit encryption algorithm aesctr aesctrhmac followed bit


example html


video srcudp2391921595000 encryptionalgorithmtsaesecb encryptionkey01030507090b0d0f00020406080a0c0e


note
video player longer accepts encryption key bottom bit identical

example javascript


player documentgetelementbyidmyvideoplayer
playersetattributeencryptionalgorithm tsaesecb
playersetattributeencryptionkey 01030507090b0d0f00020406080a0c0e


## Video Stream Parsing

following optional attribute included html video preferredvideo preferredaudio preferredcaptions multiple video audio data stream encapsulated video input attribute allow determine stream example video contain english spanish audio track preferredaudio attribute specify spanish track played exists video defaulting english otherwise

preferred stream chosen matching supplied text pattern textual description stream

attribute preferredvideo preferredaudio preferredcaptions semicolonseparated list template

template commaseparated list pattern

pattern fieldnamefieldvalue pair matched directly stream description


### Video Streams

template preferredvideo attribute contain following pattern

pidinteger packet identifier video stream wish display

programinteger program number video stream

codecvideocodec preferred video codec following

mpeg1

mpeg2

mpeg4part2

h263

h264



h265

widthinteger preferred video width

heightinteger preferred video height

aspectfloatxyy preferred aspect ratio video stream floatingpoint number fractional digit

colordepthinteger preferred color depth video


example


preferredvideopid7680 codech264 width1280 height720 aspect178 colordepth8


### Audio Streams

template preferredaudio attribute contain following pattern

pidinteger packet identifier audio stream wish play

programinteger program number audio stream

codecaudiocodec preferred audio codec following

mpeg





aacplus



ac3plus





flac

vorbis

channelsinteger preferred number audio channel

freqfrequency preferred sample frequency audio track following

32000

44100

48000

langlanguage code determines preferred language audio track language code specified 6392 standard

typeaudiotype preferred audio type following

main audio

clean effect

hearing impaired

visual impaired commentary


example


preferredaudiopid4192 codecac3 channels5 freq48000 langeng typemain audio


### Subtitle and Caption Streams

template preferredcaption attribute contain following pattern

pidinteger packet identifier caption stream wish play

typesubtitletype encoding standard subtitle value following

cea708 cea708 standard present subtitletype default cea608 present

cea608



langlanguage code determines preferred language subtitle language code specified 6392 standard

serviceinteger preferred service number caption stream


example


preferredcaptionspid0 typecea708 langeng service1


note
subtitle caption rendered graphic layer must zindex zindex place video behind graphic otherwise subtitle andor caption covered video

### Pattern Matching Behavior

note following matching template stream description

template match stream description every pattern within template must match

first listed template match stream description used

empty template string match stream description

value comparison caseinsensitive

numerical value must match stream description exactly without leading zero example pattern pid016 never match stream value

indicate logical negation apply exclamation mark beginning pattern example specifying preferredvideocodech265 match stream encoded using h265

apply greaterthan symbol integer indicate successful match value stream description must greater value following symbol example specifying preferredvideowidth1921height1081 match video larger fullhd

apply lessthan symbol integer indicate successful match value stream description must less value following symbol


### Further Examples

following template list contains three pattern langeng langspa empty string first pattern specifies english language channel english channel exist second pattern specifies spanish language channel third pattern specifies channel first dont exist empty string match anything


preferredaudiolangenglangspa


since following template list empty caption specified used disable caption altogether


preferredcaptions


following template list contains empty string template since empty template match anything first video stream encountered played default behavior attribute


preferredvideo


following template list specifies 48khz audio stream otherwise audio stream played observe list terminated semicolon case semicolon implicitly supplied


preferredaudiofreq48000


following template list contains template note pattern within template must match stream description entire template match example aacencoded english track preferred mp3encoded english track designated second option track chosen neither template matched


preferredaudiocodecaaclangengcodecmp3langeng


## Video Track Switching

brightsign medium playback framework support dynamic switching among track html5 videoaudio however support querying track information using tracklist following step outline select track using

create video element javascript attached invisible

onloadedmetadata event listener

medium

call load html5 video element trigger loadedmetadata event

read track information event

create html5 video player track information preferredaudio preferredvideo preferredsubtitle parameter described

call loadplay video element

append video element


note
switching video another important video source blank release video element otherwise first video continue memory subsequent video playing line code example

example


doctype html
head
script
video

function playtracknext

switch audiovideo
videovideotracks1id
audiopid videoaudiotracks1id
release video element
videosrc
create video element
video documentcreateelementvideo
videosrc
videohwz
videopreferredvideo
params gathered previous video load
videopreferredaudio audiopid
videoload
videoplay
documentgetelementbyidvideoareaappendchildvideo



function runtest

initialize testing bsjavascript bridge
bsstart
initial load medium gather track information
video documentcreateelementvideo
videoonloadedmetadata playtracknext play track
videosrc
videohwz
videoload trigger loadedmetadata event video loaded

script
head
html
body bgcolore6e6fa onloadruntest
h1video audio track test pageh1
idvideoareadiv
html


## Audio Routing <audio>/<video> Elements

brightsign player unique audio attribute audiovideo element allow control audio routed player output

pcmaudio audio

compaudio compressed audio

multiaudio multichannel audio


attribute passed following value determine audio routed

none

hdmi hdmi1 hdmi2 hdmi3 hdmi4 series player multiple output



spdif

analog

analogn specifies port enumeration useful model multiple analogaudio port also analog1 specify analog output model single analogaudio port


note
dont assign audio attribute audiovideo element audio routed audio output along audio currently playing

example


video srcexamplemoviemp4 width512 height400 pcmaudiohdmi autoplay
browser support video
video


example


video srcexamplemoviemp4 width512 height400 compaudiohdmiusbautoplay
browser support video
video


## HTML Video Timecode Playback

brightsign precision html video timecode playback 200ms

## Chroma Keying

brightsign chroma setting consist mask minimum maximum value minimum maximum important value since mask really useful special effect pixel every frame checked minimum maximum value pixel fully transparent outside range pixel fully opaque mean hard edge gradual fade video go opaque transparent

#### Chroma Key Tips

better chroma keying antialias pixel transparent able target single transparency color rather range

video compressed chroma subsampled edge chroma intermediate value green frame color animation green hole often antialiasing result fade green around edge able chroma keyed edge value shown example example rovideoplayerdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideoplayermd object

easiest color remove content black luma value video subsampled chroma rather using luma keying mean every pixel accurately keyed

white luma quite full range value chroma mean contains many bright color hard remove white

arbitrary color hard deal involve specifying small range chroma value must calculated color removed calculated ycbcr value used chroma keying source range used tight since single color made transparent video source live footage shot green screen range need much wider accommodate range green color video


#### Examples

##### Lower Chroma Key Values

range range leave green halo around area blended give smoother look since chroma keying cant smooth transition


vsetkeyingvaluecrhff2000 cbhff3000


##### Higher Chroma Key Values

example cover much larger range color


vsetkeyingvaluecrhff7000 cbhff7000


developersdevelopershtmldevelopmentknownissuesmd
# Known Issues

brightsigns html5 rendering engine constant workinprogress following known issue working resolve future version player firmware

## Rotated 4K Output

displaying html page rotated video using output mode cause video glitch case even video part html page displayed rotated using brightscript

## Localized JavaScript Time

javascript tolocaletimestring call retrieve localized time format 24hour 12hour clock instead hourminute clock default 24hour time brightsign player code provides workaround javascript would like display time using 12hour clock


function format12hourdate

zero

dategethours
dategetminutes
dategetseconds

ifhh


else


zero value
zerohhslice2
zerommslice2
zerossslice2

return dategethours



would prefer display second information replace return line following


return dategethours


implement function html script follows


datestring startjsdategetmonth
startjsdategetdate
startdatetimeisdateonly
datestring format12hourstartjsdate



developersdevelopershtmldevelopmentnodejsversionsmd
# Node.js Versions

brightsignos version node shipped player

nodejs version integrated chromium

standalone nodejs used ronodejs similar object


version number identical although brightsign try ensure least major version

note embedded nodejs associated rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd standalone nodejs associated ronodejsdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsronodejsmd

## Determining Version Numbers

inspecting processversion environment reliable determine exact version number given version standalone nodejs enter processversion prompt


brightsign node
processversion
v10153

brightsign



embedded nodejs script print version number inspect output type directly console


brightsign htmlplay datatexthtmlscriptconsolelogprocessversionscript
brightsign

12173535688 info source datatexthtml3cscript3econsolelogprocessversion3cscript3e1 v10110
brightsign


## OS/Chromium Version Compatibility

brightsignos version chromium version embedded nodejs version standalone nodejs version

chromium
chromium 1000
chromium 10110 10153
chromium 14176 14176

developersdevelopershtmldevelopmentnodejsmd
# Node.js



table content

brightsign nodejs implementationbrightsignnodejsimplementation
enabling nodejsenablingnodejs
crossdomain securitycrossdomainsecurity
storagewebstorage
jqueryjquery
node serialportnodeserialport
reloading nodejs enabled applicationsreloadingnodejsenabledwebapplications
packaging delivering nodejs applicationspackaginganddeliveringnodejsapplications
webpackwebpack
device storage pathsdevicestoragepaths
debugging applicationsdebuggingapplications
downloading large filesdownloadinglargefiles
nodejs examplesnodejsexamples

customer often need communicate application brightsign player brightsign player outside world done using various protocol http serial popular write application either brightscript javascript create functionality choose write application javascript need nodejs implement feature hosting server javascript

brightsign make nodejs endpoint available partner nodejs module feature

## BrightSign Node.js Implementation

brightsign player support nodejs runtime environment run javascript engine used chromium nodejs chromium instance share single javascript execution context javascript application access nodejs module object time brightsign firmware push nodejs event chromium event loop ensuring javascript application receive nodejs event seamlessly

brightsign nodejs implementation based nwjs electron project share many characteristic whereas electron us javascript file entry point javascript file creates webview also access nodejs runtime nwjs brightsign html file entry point brightsign player brightscript creates nodejsenabled rohtmlwidget instance initial passed rohtmlwidget initialized act entry point nodejs application

like nwjs electron brightsign sandboxing instead launch render process nodejs user storage group write permission local storage read permission entire file system also access networking interface privileged port

attachmentsnodejscombineddiagramspng

integrated nodejs implementation based node documentation usage information consult nodejs 1000 documentation

note
nodejs enabled iframes worker

## Enabling Node.js

nodejs object functionality available brightauthorconnected user specify nodejs item presentation setting nodejs object available brightauthor

nodejs enabled individual rohtmlwidget instance including nodejsenabledtrue entry initialization parametersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd rohtmlwidget object

example


rcreateobjectrorectangle 0019201080

port 3000

config
nodejsenabled true
inspectorserver
brightsignjsobjectsenabled true
filesdnodehellohtml

hcreateobjectrohtmlwidget config
hshow


warning
recommend loading arbitrary website nodejs enabled javascript library assume nodejs running instance serverside capability attempt load dependency causing playback fail

note
using brightauthor plugin enable nodejs need desired parameter plugin rather html5 state example want enable mouse cursor need mouseenabledtrue rohtmlwidget initialization rather checking html5 state

### Cross-Domain Security

chromium default security measure preventing crosssite scripting attack rohtmlwidget instance remote domain javascript application domain cannot make http request domain hand point local storage request remote domain acceptable

want reference domain remote application websecurity parameter false initalizing rohtmlwidget shown

example


rcreateobjectrorectangle 0019201080

port 3000

config
nodejsenabled true
inspectorserver
brightsignjsobjectsenabled true

securityparams websecurity false

hcreateobjectrohtmlwidget config
hshow


### Web Storage

want javascript storage application need specify storagepath storagequota initializaing rohtmlwidget

example


rcreateobjectrorectangle 0019201080

port 3000

config
nodejsenabled true
inspectorserver
brightsignjsobjectsenabled true
filesdnodehellohtml
storagepath
storagequota 1073741824

hcreateobjectrohtmlwidget config
hshow


### JQuery

jquery requires workaround operate correctly nodejs page example workaround requires modifying content dont control webpage enabling node html widget cause intractable problem enable nodejs planning example javascript apidevelopersplayerapisjavascriptapismds

also html best practiceshtmldevelopmenthtmlbestpracticesmd

### Node SerialPort

brightsign player provides javascript serial port binding node serialport package binding used using brightsignserialport


const serialport requireserialportstream
const brightsignbinding requirebrightsignserialport
serialportbinding brightsignbinding


also reference implementation github

### Reloading Node.js Enabled Web Applications

customer application us brightsign object object throw javascript exception reloaded brightsignos even though worked earlier limitation native module node problem fixed ship node also disable nodejs brightsign object dont need

## Packaging and Delivering Node.js Applications

warning
using electronchromium later version brightsign longer support brightscriptjavascript object iframes security reason iframes request sent parent parent page call brightsignjavascript object

deploy nodejs application brightsign player install computer create nodemodules directory copy directory card along rest application

initialized brightsign nodejs implementation seek nodemodules directory relative loaded html file like standard nodejs application load module contained nodemodules directory

note
majority nodejs module contain javascript code however module contain binary code module containing binary part installed using install binary part compiled local platform usually intel code brightsign player currently brightsign nodejs implementation limited javascript code

### WebPack

nodemodules directory associated nodejs application contain hundred thousand unnecessary file webpack bundler allows reduce nodemodules directory manageable size

webpack need place nodejs entrypoint function separate file indexjs rather inline html file contain reference javascript file nodejs module

example indexjs


myutils requireutilities utilitiesjs
moment requiremoment node module

function main

myutilsfoo
momentnow




javascript file containing nodejs entry point referenced html file

example html


script srcindexjsscript


webpack attach main window object found html file


myutils requireutilities utilitiesjs
moment requiremoment node module

function main

myutilsfoo
momentnow


windowmain main


change html file point bundled javascript windowmain


script srcbundlejsscript

body onloadwindowmain


build bundle following step computer


webpack webpackcli
webpack mode production


publish indexhtml bundlejs file there need publish nodemodules directory sample webpack configuration information

webpackconfigjsattachmentswebpackconfigjs

## Device Storage Paths

load nodejs module readwrite file must first define root directory device storage following common root directory

microsd storagesd

storagessd

storageusb1


recommend using processchdir call beginning script change process path

example


process requireprocess
processchdirstoragesd



alternatively module located multiple storage drive append multiple search path module

example


modulepathspushstoragesd
modulepathspushstoragessd
modulepathspushstorageusb1


## Debugging Applications

nodejs module enabled become visible chromium remote inspector allowing debug application consolelog work like normal application output redirected stderr remote inspector

## Downloading Large Files

application us xmlhttprequest object download large file 100200mb depending player model player memory download operation fail xmlhttprequest object first downloads whole file memory creates blob object equal size memory requirement download effectively double file size

largefile downloads recommend using fetch callback fired fragment downloaded data appended disk arrives player wont memory matter file size downloadtest htmljavascript example us fetch nodejs file service module download file fragment

downloadtestzipattachmentsdownloadtestzip

note
example specific brightsign player requires nodejs runtime enabled rohtmlwidget nodejsenabled flag write file disk

## Node.js Examples

github contains nodejsstarterproject project originally created brightauthor also used brightauthorconnected

another example script initializes http server brightsign player port 8000 client example desktop browser connects server send model number boot version player client script also display address connected client screen attached player

example


html
script
function displaymessage

load http module create http server
http require

configure http server respond hello world request
server request response
deviceinfo bsdeviceinfo
responsewritehead200 contenttype textplain
responseenddevice informationn deviceinfomodel deviceinfobootversion
requestconnectionremoteaddress
documentgetelementbyidipinnerhtmlserver responded
consolelogserver responded request


listen port 8000 default 127001
serverlisten8000

display brightsign browser
requireos
interface osnetworkinterfaces
address
interface
interfacesk
address interfaceskk2
addressfamily ipv4 addressinternal
addressespushaddressaddress



message server running addresses0 8000br
documentgetelementbyidipinnerhtml message

print message console
consolelogmessage


script
body stylebackgroundcolorred onloaddisplaymessage
stylefontsize60px textaligncenter

body
html



builtin module initialized using require method nodejsenabledtrue entry included initializing rohtmlwidget object shown require method available

developersdevelopershtmldevelopmentmd
# HTML Development

brightsign player feature chromium html rendering engine allowing display local remote html page single fullscreen page html content presentation display html content within brightauthor zone along multimedia content feature greatly increase creative option using brightsign player

contained page generalpurpose instruction writing html code using html publishing software section html presentation ensure html content work seamlessly brightsign player

page information chromium option series player

reference implementation detail found github repository

developersdeveloperslocalandremotediagnosticwebserverapismd
# Local and Remote Diagnostic Web Server APIs

apis allow connect individual brightsign player especially useful many device network quickly find access player

local apislocalandremotediagnosticwebserverapislocaldwsapismd access player local network apis give information player reboot player health card access functionality call underlie brightauthorconnected local apis include presentation autorun server apis hosted presentation autorun accessed authentication local brightscript object presentation autorun know respond request local apis local player apis authenticated username password oauth bearer token


screenshot 20230317 91213 ampngattachmentsscreenshot202023031720at209121320ampng

remote apislocalandremotediagnosticwebserverapisremotedwsapismd contained websockets apis websocket connection leverage legacy endpoint would otherwise addressable local network connection established brightsign websockets server send websockets message brightsign player depending operation brightsign player return information brightsign websockets server relayed server rest response client application

remote apis allow access player bsncloud using bearer token bsncloud well information player reboot player health card access functionality call underlie brightauthorconnected


wsapiv3pngattachmentswsapiv3png

developersdevelopersplayerapisbrightscriptjavascriptobjectsbsbtmanagermd
# BSBtManager

bsbtmanager object discover whether adapter present receive event example adapter added removed also used retrieve modify bluetooth advertising

## Attributes

bsbtmanager object following attribute

readonly attribute array adapter list available bluetooth adapter list empty adapter present

## Events

onbtevent callback receive event

addadapter adapter added value report name adapter

startupcomplete initial advertising list built event sent initial addadapter event application wait event detecting missing adapter

removeadapter adapter removed value report name adapter

updateadvertising bluetooth advertising changed value identifies source change brightscript javascript script maintains variable containing advertising list event indicates need refreshed

note
since additional event added future script capacity handle unrecognized event

### Example

btmonbtevent function consolelogevent evname parameter evparameter

## Methods

bsbtmanager object following method

object getcurrentadvertising

return bsbtadvertisementlist object containing current advertisement parameter

boolean startadvertisingin object advertisementlist

begin sending advertisement using specified bsbtadvertisementlist object calling method replace previous advertisement including persistent advertisement regardless whether javascript brightscript preserve advertisement retrieve current bsbtadvertisementlist make change needed passing startadvertising

startadvertisingnew bsbtadvertisementlist

stop advertisement

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

bsbtadvertisementlist

bsbtadvertisementlist object container bsbtadvertisement object element added list using push removed using existing element accessed indexing

bsbtadvertisement

bsbtadvertisement object represents single advertisement support advertising data standard format arbitrary custom value standard format value initialized construction using dictionary advanced custom field must object supported mode described

### Beacon Format

mode us simple beaconing format

modebeacon

beaconuuid string representation uuid 16bit 32bit 128bit format 16bit uuid must exactly four digit punctuation 32bit uuid must exactly eight digit punctuation 128bit uuid must punctuated exactly follows cd7b6f81f7384cadaebfd2a2ea36d996

beaconmajor integer specifying 2byte major value 65535

beaconminor integer specifying 2byte minor value 65535

beaconleveloptional 8bit signed integer corresponds measurement power level meter default level

beaconmanufactureroptional 2byte integer value 65535 specifying beacon manufacturer default value

connectableoptional boolean value indicating whether advertisement connectable gatt service advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot beacon advertisement persistent default

### Eddystone-URL Format

mode us eddystoneurl format

modeeddystoneurl

encapsulate advertisement packet long packet startadvertising call return aborterror exception includes description compressed long

txpoweroptional integer value specifying power level meter default value corresponds level 60dbm meter recommended calibration practice measure meter example 65dbm rssi lead value

connectableoptional boolean value indicating whether advertisement connectable gatt service advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot eddystoneurl advertisement persistent default

### Eddystone-UID format

mode us eddystoneuid format

modeeddystoneuid

namespace 10byte value expressed hexadecimal digit

instance 6byte value expressed hexadecimal digit

txpoweroptional integer value specifying power level meter default value corresponds level 60dbm meter recommended calibration practice measure meter example 65dbm rssi lead value

connectableoptional boolean value indicating whether advertisement connectable gatt service advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot eddystoneurl advertisement persistent default

### Custom Format

mode support arbitrary custom data binary field specified hexadecimalencoded string decimal value would specified 0c80 list support pushpop call indexing duplicate value included

modecustom

manufacturerdataoptional bsbtmanufacturerdata object containing following field

manufacturer unsigned 16bit integer value

data binary data

serviceuuidoptional list uuid string

servicedataoptional bsbtuuiddata object containing following field

uuid uuid string

data binary data

soliciituuidoptional list uuid string

connectableoptional boolean value indicating whether advertisement connectable gatt service advertisement nonconnectable default

persistentoptional boolean value indicating whether advertisement persist every reboot custom advertisement persistent default


## Examples

script configures simple advertisement eddystoneurl advertisement begin advertising


bsbtadvertisementlist
bsbtadvertisement mode beacon beaconuuid 41fac221c8cb41e7b01112d1016dd39e beaconmajor beaconminor
adspushad1
bsbtadvertisement modeeddystoneurl
adspushad2

btmstartadvertisingads


script find beacon matching uuid form string majorminor code



fori adlistlength
adlistimode beacon
adlistibeaconuuid 434b2eb8c28f40898e7a1e644bb13b9f
beacon adlistibeaconmajor adlistibeaconminor




script look eddystoneurl beacon sends update based current


bsbtmanager
adlist btmgetcurrentadvertising
fori adlistlength
brightsignbiz
adlistimode eddystoneurl adlistiurl
adlistiurl


btmstartadvertisingadlist


script produce exception compressed long


bsbtadvertisementlist
bsbtadvertisement mode eddystoneurl
alpushad4
bstartadvertisingal


developersdevelopersplayerapisbrightscriptjavascriptobjectsbscecreceivermd
# BSCECReceiver

information available method refer rocecinterfacedevelopersbrightscriptobjectreferenceinputoutputobjectsrocecinterfacemd entry note javascript class receive message bscectransmitterbrightscriptjavascriptobjectsbscectransmittermd send message

javascript equivalent cecplayerapisjavascriptapiscecmd

## Events

following event available bscecreceiver object receive event type cecreceiverevent

onececrxframe

oncectxcomplete

### BSCECReceiverEvent – Attributes

readonly attribute status

readonly attribute domstring data

### BSCECReceiverEvent – Methods

arraybuffer getbytes

## Methods

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Example


script
function loadcec

consolelog loadcec

cecin bscecreceiver

cecinoncecrxframe functione
consolelog oncecrxframe edata


cecinoncectxcomplete functione
consolelog oncectxcomplete estatus


script


developersdevelopersplayerapisbrightscriptjavascriptobjectsbscectransmittermd
# BSCECTransmitter

information available method refer rocecinterfacedevelopersbrightscriptobjectreferenceinputoutputobjectsrocecinterfacemd entry note javascript class send message bscecreceiverbrightscriptjavascriptobjectsbscecreceivermd receive message

possible javascript apis used instead brightscriptjavascript object javascript equivalent object cecplayerapisjavascriptapiscecmd

## Methods

boolean sendrawmessagein arraybuffer data

boolean sendrawmessagein arraybufferview data

boolean sendrawmessagein domstring data

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Example

following javascript example show send message


function cecdisplayon

consolelog cecdisplayon
ceccontrol bscectransmitter
buffer uint8array2
buffer 0x40
buffer 0x0d
ceccontrolsendrawmessagebuffer


function cecdisplayoff

consolelog cecdisplayoff
ceccontrol bscectransmitter
buffer uint8array2
buffer 0x40
buffer 0x36
ceccontrolsendrawmessagebuffer



developersdevelopersplayerapisbrightscriptjavascriptobjectsbscontrolportmd
# BSControlPort

object provides support bp200bp900 button board gpio port button press returned oncontroldown oncontrolup event object used configure output level connector monitor input typically led button attached gpio connector brightsign player brightsign expansion module

javascript equivalent controlportplayerapisjavascriptapiscontrolportmd

## Object Creation

rocontrolport object created single parameter specifies port used


bscontrolportin domstring portname


port parameter following

brightsign specifies onboard gpio connector including gpio12 button

expandergpio specifies db25 connector brightsign expansion module brightsign expansion module attached object creation fail invalid returned

expanderngpio specifies usbtogpio device connected player multiple usbtogpio device controlled using separate rocontrolport instance first device corresponds expander0gpio second expander1gpio

expanderdip specifies eight switch brightsign expansion module brightsign expansion module attached object creation fail invalid returned


note
hotplugging brightsign expansion module supported

touchboardngpio retrieves event specified bp200bp900 button board event handled manner event brightsign port

touchboardnledsetup set various output option specified bp200bp900 button board

touchboardnled set bit button specified bp200bp900 button board bit indicate whether associated


note
since multiple bp200bp900 button board connected player simultaneously value specifies port enumeration board value corresponds value returned rodeviceinfogetusbtopologydevelopersbrightscriptobjectreferencesystemobjectsrodeviceinfomd method unspecified enumeration value synonymous button board enumeration value touchboardgpio touchboard0gpio identical

## Methods


page table pin corresponding button onboard gpio connector

boolean configureasinput unsigned button

mark specified button input invalid button number passed false returned successful function return true input button tristated driven high externally

boolean configureasoutput unsigned button

mark specified button output invalid button number passed false returned successful function return true output driven high depending current output state

boolean setpinvalueunsigned button unsigned output

configures output specified button either high button configured output resulting level undefined method also used configure output behavior bp200b900 button boardsdevelopersbrightscriptobjectreferenceinputoutputobjectsrocontrolportmd

boolean getpinvalueunsigned button

return output specified button

void close

shuts bscontrolport instance preventing consuming resource method called garbage collection determines instance destroyed

boolean setoutputvalueunsigned param

specifies desired state output attached control port bit integer individual button using binary operation

parameter 8bit integer represents output

boolean setoutputvaluesunsigned param1 unsigned param2 unsigned param3 unsigned param4

configures button bp200bp900 button board method used bscontrolport object instantiated touchboardnledsetup touchboardnled parameter parameter integer value

## Events

following event available bscontrolport object event receive controlportevent event

oncontroldown

oncontrolup

oncontrolevent


### ControlPortEvent – Attributes

readonly attribute unsigned long code


## Examples

following example code configures four gpio output


gpio bscontrolportbrightsign

output
gpioconfigureasoutput0
gpioconfigureasoutput1
gpioconfigureasoutput2
gpioconfigureasoutput3

desired state
gpiosetpinvalue0
gpiosetpinvalue1
gpiosetpinvalue2
gpiosetpinvalue3


following example cause led bp900 button board twinkle


bp900gpio
function myfunction

bp900setup bscontrolporttouchboard0ledsetup
bp900setupsetpinvalue0

bp900 bscontrolporttouchboard0led
bp900setpinvalue0 0x07fe
bp900setpinvalue1 0x07fd
bp900setpinvalue2 0x07fb
bp900setpinvalue3 0x07f7
bp900setpinvalue4 0x07ef
bp900setpinvalue5 0x07df
bp900setpinvalue6 0x07bf
bp900setpinvalue7 0x077f
bp900setpinvalue8 0x06ff
bp900setpinvalue9 0x05ff
bp900setpinvalue10 0x03ff

bp900gpio bscontrolporttouchboard0gpio
bp900gpiooncontroldown functione

consolelog oncontroldown ecode




following example display event gpio expander board note using equivalent rogpiocontrolport object brightscript time result unpredictable behavior


html
head
script
bp900gpio bscontrolportbrightsign

bp900gpiooncontroldown functione
consolelog oncontroldown ecode
newtext ecode
documentmyformoutputtextvalue newtext
documentmyformoutputtextscrolltop documentmyformoutputtextscrollheight


bp900gpiooncontrolup functione
consolelog oncontrolup ecode
newtext ecode
documentmyformoutputtextvalue newtext
documentmyformoutputtextscrolltop documentmyformoutputtextscrollheight


bp900gpiooncontrolevent functione
consolelog oncontrolevent ecode
newtext event ecode
documentmyformoutputtextvalue newtext
documentmyformoutputtextscrolltop documentmyformoutputtextscrollheight


function ledonoutputindex

bp900gpioconfigureasoutputoutputindex
newtext outputindex
documentmyformoutputtextvalue newtext
documentmyformoutputtextscrolltop documentmyformoutputtextscrollheight


function buttononoutputindex

bp900gpioconfigureasinputoutputindex
newtext input outputindex
documentmyformoutputtextvalue newtext
documentmyformoutputtextscrolltop documentmyformoutputtextscrollheight

script
head

body bgcolore6e6fa

h1gpioexpander test pageh1
note play well emrogpiocontrolportembrbr
input typebutton onclickledon0 valueled0
input typebutton onclickledon1 valueled1
input typebutton onclickledon2 valueled2
input typebutton onclickledon3 valueled3
input typebutton onclickledon4 valueled4
input typebutton onclickledon5 valueled5
input typebutton onclickledon6 valueled6
input typebutton onclickledon7 valueled7

input typebutton onclickbuttonon0 valuebutton0
input typebutton onclickbuttonon1 valuebutton1
input typebutton onclickbuttonon2 valuebutton2
input typebutton onclickbuttonon3 valuebutton3
input typebutton onclickbuttonon4 valuebutton4
input typebutton onclickbuttonon5 valuebutton5
input typebutton onclickbuttonon6 valuebutton6
input typebutton onclickbuttonon7 valuebutton7


form namemyform
textarea readonly rows50 cols100 nameoutputtext stylefontfamilymonospacetextarea
form

body
html


developersdevelopersplayerapisbrightscriptjavascriptobjectsbsdatagramsocketmd
# BSDatagramSocket

information available method refer rodatagramreceiver rodatagramevent entry

## Methods

boolean bindlocalportin long port

long getlocalport

boolean joinmulticastgroupin domstring group

boolean sendtoin domstring dest long port arraybufferview data

boolean sendtoin domstring dest long port domstring data

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Events

following event available bsdatagramsocket object receive event type datagramsocketevent getbytes retrieve body message

ondatagram

### DatagramSocketEvent

datagramsocketevent following attribute

readonly attribute domstring remotehost

readonly attribute remoteport

datagramsocketevent support following method

arraybuffer getbytes

## Example

note
learn convert string arraybuffer


bssocketmessage bsdatagramsocket
bssocketmessagebindlocalport1234
bssocketmessageondatagram functione

txtdec textdecoderutf8
consolelogreceived txtdecdecodeegetbytes



developersdevelopersplayerapisbrightscriptjavascriptobjectsbsdeviceinfomd
# BSDeviceInfo

information available method refer rodeviceinfo entry javascript equivalent deviceinfoplayerapisjavascriptapisdeviceinfomd

## Attributes

readonly attribute domstring model

readonly attribute domstring version

readonly attribute deviceuptime

readonly attribute devicelifetime

readonly attribute devicebootcount

readonly attribute domstring bootversion

readonly attribute domstring deviceuniqueid

readonly attribute domstring family

## Methods

versioncomparein domstring version

bootversioncomparein domstring version

boolean hasfeaturein domstring feature

## Example

following javascript example post device information page button clicked


function deviceinfo

deviceinfo bsdeviceinfo
documentgetelementbyidmodeltextinnerhtml deviceinfomodel
documentgetelementbyidversiontextinnerhtml deviceinfoversion
documentgetelementbyidbversiontextinnerhtml deviceinfobootversion
documentgetelementbyidserialtextinnerhtml deviceinfodeviceuniqueid
documentgetelementbyidfamilytextinnerhtml deviceinfofamily

documentgetelementbyiduptimeinnerhtml deviceinfodeviceuptime
documentgetelementbyidlifetimeinnerhtml deviceinfodevicelifetime
documentgetelementbyidbootcountinnerhtml deviceinfodevicebootcount

ifdeviceinfoversioncompare4736

documentgetelementbyidversion1innerhtml version 4736

else

documentgetelementbyidversion1innerhtml version 4736


ifdeviceinfohasfeaturesix channel audio

documentgetelementbyidfeatureinnerhtml channel audio available

else

documentgetelementbyidfeatureinnerhtml channel audio available




developersdevelopersplayerapisbrightscriptjavascriptobjectsbsirreceivermd
# BSIRReceiver

class receives event information refer object reference manual entry roirreceiver

## Object Creation

bsirreceiver object must specify hardware interface receive event well encoding look

bsirreceiverdomstring interface domstring encoding


valid hardware interface include following

gpio gpio connector

irin 35mm inputoutput connector

iguana iguanaworks transceiver source support encoding simultaneously

tvcontroller virtual driver available brightsign builtin product read message uart drive roirreceiver object like receiver creation example would



bsirreceivertvcontroller


valid encoding include following multiple encoding specified string using



supported iguanaworks device


code expressed bit

bit button code

bit manufacturer code


note
manufacturer code zero code considered intended roku soundbridge remote control

## Methods

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Events

event available bsirreceiver object event receive irreceiverevent event

onremotedown

onremoterepeat

onremoteup supported iguanaworks device

#### IRReceiverEvent – Attributes

readonly attribute domstring irtype

readonly attribute unsigned long code

## Example

following javascript example display message remote code received


function myfunction

irreceiver bsirreceiveririnnec

irreceiveronremotedown functione
consolelog onremotedown eirtype ecode


irreceiveronremoteup functione
consolelog onremoteup eirtype ecode




developersdevelopersplayerapisbrightscriptjavascriptobjectsbsirtransmittermd
# BSIRTransmitter

class receives event information refer object reference manual entry roirtransmitter

## Object Creation

bsirtransmitter object must specify hardware interface output signal

bsirtransmitter domstring interface

valid hardware interface include following

irout 35mm input connector available xdx30 player 35mm inputoutput connector available xtx43 4kx42 xdx33 xdx32 player

iguana iguanaworks transceiver


## Methods

boolean sendin domstring type unsigned long code

boolean setsendpolarityin boolean polarity

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Example


script
irtransmitter bsirtransmitterirout

function ircode1

consolelog ircode1
irtransmittersendnec 65284

function ircode2

consolelog ircode2
irtransmittersendnec 65288

function ircode3

consolelog ircode3
irtransmittersendnec 65290

script


developersdevelopersplayerapisbrightscriptjavascriptobjectsbsmessageportmd
# BSMessagePort

object allows associative array passed javascript brightscript vice versa bsmessageport instance created rohtmlwidget instance

javascript equivalent messageportplayerapisjavascriptapismessageportmd

## Methods

boolean postbsmessagein dictionary message

note
postbsmessage method accept nested dictionary true postjsmessage brightscript method

## Events

following event occurs message sent brightscript javascript appear messageportevent event

onbsmessage

### MessagePortEvent

event contains single field

readonly attribute data

following script iterate field received event


bsmessage bsmessageport

bsmessageonbsmessage functionmsg

forname msgdata

consolelog name msgdataname




brightscript rohtmlwidgetpostjsmessage method used post message javascript

widgetpostjsmessage param1 data1 param2 data2 param3 data3

## Examples

following script send collection property brightscript


function myfunction

bsmessage bsmessageport
bsmessagepostbsmessagecomplete true result pas



message appear brightscript rohtmlwidgetevent case getdatareason equal message getdatamessage contains roassociativearray


finished
mpwaitmessage30000
typeev rohtmlwidgetevent
print typeev
stop

payload evgetdata
print payload
print reason payloadreason
payloadreason message
print message payloadmessage
payloadmessagecomplete invalid
stop
else payloadmessagecomplete true
finished true
payloadmessageresult pas
print test passed
else
print test failed payloadmessageerr
stop






developersdevelopersplayerapisbrightscriptjavascriptobjectsbsserialportmd
# BSSerialPort

information available method refer roserialportdevelopersbrightscriptobjectreferenceinputoutputobjectsroserialportmd entry

possible brightsignserialport node package serialport instead bsserialport basic reference implementation found github repository

## Object Creation

bsserialportin unsigned long port

## Methods

void setbaudratein unsigned long baudrate raisesdomexception

void setdatabitsin unsigned long databits raisesdomexception

void setstopbitsin unsigned long stopbits raisesdomexception

void setparityin domstring parity raisesdomexception

boolean setechoin boolean flag boolean

setinvertedin boolean flag boolean

setflowcontrolin boolean flag

void setgeneratebyteeventin boolean flag raisesdomexception

void setgeneratelineeventin boolean flag raisesdomexception

void setlineendingin domstring raisesdomexception

boolean sendbytein unsigned long byte

boolean sendbytesin arraybuffer data

boolean sendbytesin arraybufferview data

boolean sendbytesin domstring data

boolean sendbreakin long durationms

void flush raisesdomexception

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

## Events

following event available bsserialport object event receive serialportevent event

onserialbyte

onserialline

### SerialPortEvent – Attributes

onserialbyte event

readonly attribute unsigned long sbyte

onserialline event

readonly attribute domstring sdata

## Example


function serialout

consolelog serialout

first externally connected port cheetah
serialout bsserialport2

serialoutsetbaudrate115200
serialoutsetdatabits8
serialoutsetstopbits1
serialoutsetparitynone
serialoutsetechotrue

serialoutsetgeneratebyteeventtrue
serialoutsetgeneratelineeventtrue

serialoutonserialbyte functione
consolelog onserialbyte esbyte


serialoutonserialline functione
consolelog onserialline esdata


serialoutsendbyte89
serialoutsendbyte90
serialoutsendbyte91

serialoutsendbyteshello world
serialoutsendbytesstringfromcharcode64



developersdevelopersplayerapisbrightscriptjavascriptobjectsbssyncmanagermd
# BSSyncManager

information available method refer rosyncmanager entry enable genlock javascript pas bssyncmanagerrosyncmanager domain videooutputsetsyncdomainplayerapisjavascriptapisvideooutputmd method

## Object Creation

bssyncmanagerin domstring interface domstring domain domstring multicastaddress domstring multicastport

setting interface empty interface omitting interface parameter equivalent specifying empty interface name

## Methods

void setasleaderin boolean leadermode raisesdomexception

void synchronizein domstring unsigned long msdelay raisesdomexception

void close

shuts instance preventing consuming resource method called garbage collection determines instance destroyed

bindtointerfacein domstring interface

bind syncmanager specific network interface example eth0 wifi0 setting interface empty interface

boolean setencryptionenablein boolean enable

boolean setencryptionenablein boolean enable domstring

boolean setencryptionenablein boolean enable arraybuffer

enables disables encryption bssyncmanager message network method return true success false failure

specified string binary array alternatively value supplied case pseudorandomly generated used setting enable false supplying time cause method fail

encryption available enabled default later note following behavior mixedversion environment

follower unit encryption enabled ingest unencrypted synchronization message leader unit follower unit receives encrypted packet longer accept unencrypted packet leader unit unless encryption explicitly disabled using method

follower unit encryption disabled support encryption cannot ingest encrypted message leader unit therefore synchronization group includes mixed version leader unit always older version follower unit


boolean setencryptionenablewithobfuscatedkeyin domstring obfuscatedkey boolean

enables encryption bssyncmanager message using obfuscated contact supportbrightsignbizmailtosupportbrightsignbiz learn generating obfuscation storing player

## HTML Video Functions

setsyncparamsin domstring domain domstring domstring isotimestamp

html video tag include setsyncparams function calling function synchronizes video specified sync group

## Events

following event available bssyncmanager object receive event type bssyncmanagerevent

onsyncevent

### BSSyncManagerEvent – Attributes

following attribute relevant onsyncevent event

readonly attribute domstring domain

readonly attribute domstring

readonly attribute domstring isotimestamp

## Examples

following javascript example contains video synchronized locally bssyncmanager follower player configured domain leader player us follower html script display video sync leader player implemented multiple follower player

### Leader Script


video idone hwzon
source idonesrc srcpiratesmov
video

script
create sync manager provided multicast setting
sync bssyncmanagerdomain1 224012610 1539

synconsyncevent function
documentgetelementbyidonesetsyncparamsedomain eisotimestamp
documentgetelementbyidoneload
documentgetelementbyidoneplay
consolelogedomain
consolelogeid
consolelogeisotimestamp


function starttimer
settimeoutfunction
restartleader
30000

function restartleader
synchronize video start playing 1000ms
syncsetasleader1
syncsynchronizesyncevent1 1000
starttimer

restartleader

script


### Follower Script


video idone hwzon
source idonesrc srcpiratesmov
video

script
create sync manager provided multicast setting
sync bssyncmanagerdomain1 224012610 1539

synconsyncevent function
documentgetelementbyidonesetsyncparamsedomain eisotimestamp
documentgetelementbyidoneload
documentgetelementbyidoneplay
consolelogedomain
consolelogeid
consolelogeisotimestamp


script

body
html


developersdevelopersplayerapisbrightscriptjavascriptobjectsbstickermd
# BSTicker

information available method refer rotextwidget entry object used display scrolling type ticker

note
object support righttoleft lefttoright example arabic hebrew scrolling mode depending language first string file added widget change scrolling direction first remove string ticker

## Object Creation

bstickerin unsigned long unsigned long unsigned long unsigned long long rotation

integer specify position ticker widget topleft corner integer specify size widget rotation parameter accepts following value rotation counterclockwise landscape mode

degree

degree

degree

degree

note
rotation parameter affect text inside ticker alter screen coordinate widget creating vertical ticker rotating ticker match portraitmode html content need coordinate parameter match rotation text

## Methods

boolean setrectanglein unsigned long unsigned long unsigned long unsigned long

modifies position size ticker widget changing size widget reset ticker animation long size widget remains unchanged modifying position interrupt ticker animation method return true success false failure

addstringin domstring

add string queue method return stringid integer used identify string removed ontickerstringremoved event generated zero return indicates method failed string adding many string without popping stack cause addstring return nonzero value exact number depends font size string maximum recommended number stored string

addsurfacein imagedata image

add bitmap image list string display image must type imagedata method return stringid integer used identify surface removed ontickerstringremoved event generated code bottom page example using canvasimage method

boolean popstringsin unsigned long count

remove designated number string queue method return true success false failure

boolean setautopopin boolean

method true string automatically removed popped stack scrolled offscreen

boolean setforegroundcolorin unsigned long argb

specifies foreground color 32bit number argb alpha green blue format method return true success false failure

boolean setforegroundcolorin unsigned long unsigned long unsigned long unsigned long

set foreground color green blue foreground alpha value currently unsupported ignored method though change future firmware version integer value method return true success false failure

boolean setbackgroundcolorin unsigned long argb

specifies background color 32bit number argb alpha green blue format method return true success false failure

boolean setbackgroundcolorin unsigned long unsigned long unsigned long unsigned long

set background color alpha green blue standard alpha value value bsticker unsigned long upper bit unsigned long value mapped 0x00 0xff correspond method return true success false failure

boolean setseparatorstringin domstring

text string separate individual message method return true success false failure

boolean setseparatorcircle

circle separate individual message method return true success false failure

boolean setseparatordiamond

diamond separate individual message method return true success false failure

boolean setseparatorsquare

square separate individual message method return true success false failure

unsigned long setpixelspersecondin unsigned long

set speed ticker

boolean setfontin domstring font

specifies font bsticker well rotextwidget brightscript object method accepts list fontfamily name similar fontfamily property string also fontface prefix indicate font description example fontfacedejavu serifserif italic bold font must added html widget using rohtmlwidgetaddfont method used bsticker instance method return true success false failure

boolean setsyncmanagerin domstring domain

specifies bssyncmanager domain executing setmultiscreen call method called creates internal domain based existing bssyncmanager domain us network parameter recommend using method instead passing multicast address port setmultiscreen method method return true success false failure

boolean setmultiscreenin unsigned long offset unsigned long size domstring ipaddress unsigned long port

call setmultiscreen method create ticker smoothly scroll across multiple screen method return true success false failure

offset determines left starting point pixel multiscreen array parameter value always leftmost display parameter calculated using length multiscreen ticker total length multiscreen display example using offset 1920 twoscreen array 1920x1080 screen would specify player righthand master displayto create ticker smoothly scroll across multiple screen call setmultiscreen method page

size total width pixel multiscreen array across display parameter value setmultiscreen call note size multiscreen ticker different total width multiscreen display example width bsticker widget smaller width screen defining size 3840 would specify twoscreen array 1920x1080 screen

ipaddress string specifying multicast address synchronization process example 23919200

port string specifying multicast port synchronization process example 1234


following example diagram code snippet specify multiscreen display monitor width monitor 1024 pixel width ticker pixel

attachmentssetmultiscreen20diagrampng

## Events

bstickerontickerstringremoved

event handler triggered string removed longer visible event contains stringid property returned successful addstring call

## Examples

following script show many available bsticker method


bsticker bsticker10

function addtext1

consolelog addtext1
bstickeraddstringaddtext1

function addtext2

consolelog addtext2
bstickeraddstringaddtext2

function addtext3

consolelog addtext3
bstickeraddstringaddtext3


function setbackground1

consolelog setbackground1
bstickersetbackgroundcolor0xffff0000

function setbackground2

consolelog setbackground2
bstickersetbackgroundcolor0xff00ff00


function setforeground1

consolelog setforeground1
bstickersetforegroundcolor0xff007700

function setforeground2

consolelog setforeground2
bstickersetforegroundcolor0xff000077


function setseparatorstring

consolelog setseparatorstring
bstickersetseparatorstring

function setseparatorcircle

consolelog setseparatorcircle
bstickersetseparatorcircle

function setseparatordiamond

consolelog setseparatordiamond
bstickersetseparatordiamond

function setseparatorsquare

consolelog setseparatorsquare
bstickersetseparatorsquare


function settickerspeed

consolelog settickerspeed
speed bstickersetpixelspersecond180
consolelog setpixelspersecond180 resulting speed speed



following example allow adding canvas image ticker addsurface method


loading canvas
canvasgetcontext2d
ctxgetimagedata0 ctxcanvaswidth ctxcanvasheight

tickeraddsurfaceimg

loading image
imageobj image
imageobjonload function
canvaswidth thiswidth
canvasheight thisheight

canvasgetcontext2d
ctxdrawimagethis getimage data

imageobjsrc filenamejpg


developersdevelopersplayerapisbrightscriptjavascriptobjectsbsvideomodemd
# BSVideoMode

information available method refer rovideomode page youd like change video mode player need brightscript instead javascript class

javascript equivalent videomodeconfigurationplayerapisjavascriptapisvideomodeconfigurationmd

## Attributes

readonly attribute resx

readonly attribute resy

readonly attribute safex

readonly attribute safey

readonly attribute safewidth

readonly attribute safeheight

readonly attribute domstring mode

readonly attribute bsdecodermodelist decodermodelist

## Methods

warning
method used object obsolete found videooutputplayerapisjavascriptapisvideooutputmd videomodeconfigurationplayerapisjavascriptapisvideomodeconfigurationmd javascript documentation hdmiaudiodisable method found rovideomode brightscript documentation


boolean isattachedin domstring connector

domstring getbestmodein domstring connector

boolean setbackgroundcolourin unsigned long

boolean setbackgroundcolourin unsigned long
unsigned long
unsigned long

boolean setpowersavemodein boolean disable

boolean hdmiaudiodisablein boolean disable

boolean setdecodermodein domstring decoder
domstring timeslicemode
zorder
domstring friendlyname
boolean enablemosaicdeinterlacer


boolean setsyncmanagerin bssyncmanager sync rovideomodesetsyncdomain entry detail


## BSDecoderMode

decodermodelist attribute contains array bsdecodermode object containing information configured decoder player

setdecodermode getdecodermode entry rovideomodedevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrovideomodemd page information decoder parameter


interface bsdecodermode
readonly attribute domstring decodername
readonly attribute domstring friendlyname
readonly attribute domstring maxsize
readonly attribute domstring configuredsize
readonly attribute unsigned long currentusage
readonly attribute unsigned long maxusage
readonly attribute boolean mosaic
readonly attribute boolean enabledeinterlacer



## Example

following javascript example illustrates retrieve information current video mode


function fillinvideodata

videomodeinfo bsvideomode
documentgetelementbyidresxinnerhtml videomodeinforesx
documentgetelementbyidresyinnerhtml videomodeinforesy
documentgetelementbyidsafexinnerhtml videomodeinfosafex
documentgetelementbyidsafeyinnerhtml videomodeinfosafey
documentgetelementbyidsafewidthinnerhtml videomodeinfosafewidth
documentgetelementbyidsafeheightinnerhtml videomodeinfosafeheight
documentgetelementbyidvideomodeinnerhtml videomodeinfomode
documentgetelementbyidbestmodeinnerhtml videomodeinfogetbestmodehdmi
documentgetelementbyidconnectedflaginnerhtml videomodeinfoisattachedvga


function changebackground

videomodeinfo bsvideomode
videomodeinfosetbackgroundcolour0xff0000



developersdevelopersplayerapisbrightscriptjavascriptobjectsenablingbrightscriptjavascriptobjectsmd
# Enabling BrightScript-JavaScript Objects

security reason brightscript javascript object disabled default result encounter error like shown enable first enable view console brightscriptjavascript event diagnostic server javascript console

attachmentsdom20exception2020console20outputpng

follow step enable brightscript javascript object

## Enabling with BrightAuthor

make sure using brightauthor version later earlier version code enables brightscript object javascript

also ensure enable external data checked within html5 state displaying page

attachmentsba2020enable20external20datapng

## Enabling with BrightScript

include brightsignjsobjectsenabledtrue entry associative array passed creation rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd instance

example


rcreateobjectrorectangle0019201080
aacreateobjectroassociativearray

aaurl
aabrightsignjsobjectsenabledtrue

bbcreateobjectroassociativearray
bbport3000
aainspectorserverbb

hcreateobjectrohtmlwidgetraa
hshow


method enables brightscriptjavascript object rohtmwidget instance enable subset brightscriptjavascript object restrict object certain url allowjavascripturls method rohtmlwidget instance method accepts associative array map brightscriptjavascript class url allowed

indicates class authorized associated url

asterisk value indicates url authorized associated brightscriptjavascript class

local value indicates local page authorized associated brightscriptjavascript class


enable brightscript class url


htmlallowjavascripturls


call enable brightscriptjavascript class local page brightsign homepage


htmlallowjavascripturls local


developersdevelopersplayerapisbrightscriptjavascriptobjectsglobalbrightscriptjavascriptfunctionsmd
# Global BrightScript-JavaScript Functions

following function implemented global level

isbslocalfilepresent

determines whether specified file exists local storage function interface brightscript pool determines file exists also search file standard name

closeallbsclasses

function effectively call close custom object created garbage collected call function initializing page ensure previous link hardware interface player removed

developersdevelopersplayerapisbrightscriptjavascriptobjectsmd
# BrightScript-JavaScript Objects

warning
application avoid using brightscript object javascript apiplayerapisjavascriptapismd object instead brightscriptjavascript migration guideplayerapisbrightscriptjavascriptmigrationguidemd mapping brightscript javascript apis

brightsign html engine expose several platformspecific javascript object allow integrate html content hardware interface system function player object allow link many standard interactive database hardware element serial device info html page

section detail function parameter javascript object information brightscript object javascript object linked brightscriptdevelopersbrightscriptmd section

developersdevelopersplayerapisjavascriptapisassetfetchermd
# assetfetcher

assetfetcher object allows downloading file asset pool represented javascript assetpooljavascriptapisassetpoolmd instance

assetfetcher


interface assetpoolfetcher
assetpoolfetcherassetpool pool
promisevoid startassetlist list assetpoolfetcherparams assetpoolparamsoptional
promisevoid cancel


interface fileevent
attribute string type
attribute string filename
attribute index
attribute responsecode
attribute string error


interface progressevent
attribute string type
attribute string filename
attribute index
attribute total
attribute long currentfiletransferred
optional attribute long currentfiletotal


interface assetpoolfetcherparams
attribute authentication auth
attribute bool enableunsafeauthentication
attribute bool enableunsafeproxyauthentication
attribute bool enableencodings
attribute bool enablepeerverification
attribute bool enablehostverification
attribute string certificatesfile
attribute headerlist header
attribute string proxy
attribute arraystring proxybypasslist
attribute unsigned progressinterval
attribute unsigned fileretrycount
attribute string relativelinkprefix
attribute string interfacename
attribute mintransferrate minimumtransferrate
attribute double maximumtransferrate
attribute bool onlyrequestcache


interface authentication
attribute string username
attribute string password


interface header
attribute string value


interface mintransferrate
attribute bytespersecond
attribute periodinseconds



## Object Creation

create assetpoolfetcher object first need create assetpool instance load brightsignassetpoolfetcher module using require method create instance assetpoolfetcher class using assetpool instance


const assetpoolclass requirebrightsignassetpool
assetpool assetpoolclasssdpool

const assetpoolfetcherclass requirebrightsignassetpoolfetcher
assetpoolfetcher assetpoolfetcherclassassetpool


## AssetPoolFetcher

interface allows start stop asset fetcher

##### start()


promisevoid startassetlist list assetpoolfetcherparams assetpoolparamsoptional


begin fetching file specified passed assetpoolassetlistjavascriptapisassetpoolmd interface fetching process configured passed assetpoolfetcherparams interface start promise return assetfetching process complete alternatively promise rejected assetpoolfetcher instance already started method cause asset pruned

##### cancel()


promisevoid cancel


cancel assetfetching process promise resolved cancellation complete

## FileEvent

interface contains information filetransfer attempt

type string contains fileevent indicate type event

filename string name asset downloaded

index zerobased index file assetpoolassetlistjavascriptapisassetpoolmd interface

responsecode protocol response code associated event following code indicate success

successful http transfer

successful transfer

successful local file transfer


note
note
also numerous error code case failure pagedevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetfetchereventmd nonexhaustive list

error string textual error message descriptive responsecode local error


## ProgressEvent

interface contains information assetfetching process

type string contains progressevent indicate type event

filename string name file currently downloaded

index zerobased index current file assetpoolassetlistjavascriptapisassetpoolmd interface

total total number file assetlist object

currentfiletransferred long number byte downloaded current asset

currentfiletotal long optional size asset byte known prior download starting provided property size known property present


## AssetPoolFetcherParams

interface contains configuration parameter assetfetcher process

auth authentication authentication interface specifying credential downloading asset

enableunsafeauthentication bool flag enabling basic http authentication http authentication us insecure protocol might allow others easily determine password assetpoolfetcher object still prefer stronger digest http supported server parameter false default setting refuse provide password basic http authentication request requiring authentication fail

enableunsafeproxyauthentication bool flag enabling basic http authentication proxy http authentication us insecure protocol might allow others easily determine password parameter false refuse provide proxy password basic http authentication request requiring authentication type fail unlike enableunsafeauthentication parameter true default

enableencodings bool flag enabling http compression communicates server system accept encoding assetpoolfetcher instance capable decoding behavior enabled default supported encoding currently include deflate gzip allow transparent compression response client assetpoolfetcher instance decoded data unaware encoding used

enablepeerverification bool flag enables checking tlsssl certificate parameter true default disabling peer verficiation allows bypass expired certificate check

enablehostverification bool flag enables checking tlsssl certificate correct hostname parameter true default disabling host verification allows accept certificate sent wrong hostname


caution
important
peer verification host verification important security check prevent maninthemiddle attack feature disabled careful consideration security implication

certificatesfile string filename alternative certificate connection method useful connection certificate signed default trusted list example organization us private hierarchy signed well known root file replaces default list passed certificate file must contain acceptable certificate required connection

header headerlist list header passed http request made assetpoolfetcher instance

proxy string name address proxy server used assetpoolfetcher instance proxy string formatted contain four character character used replace octet player current address example address currently 19216812 proxy proxy player attempt proxy named proxy192168 present setting override player global proxy setting

proxybypasslist arraystring list host exempt proxy setting list consist hostnames address cannot used assetpoolfetcher instance attempt reach specified host directly rather using proxy specified proxy parameter example hostname examplecom would exempt examplecom examplecom proxy setting present setting override global proxy bypass setting

progressinterval unsigned interval second progress event individual file downloaded setting interval null disables progress event setting interval specifies event generated often possible though slow transfer process interval positive integer event always generated start file download irrespective elapsed time default interval second

fileretrycount unsigned maximum number time file download retried moving next file download default retry count five

relativelinkprefix string prefix prepended link lack protocol assetlist object normally method used make file uris drive agnostic also used reduce size sync spec file stored place link protocol affected method

interfacename string string specifying network interface assetpoolfetcher instance network access example eth0 ethernet wlan0 wifi default behavior indicated null value send request using appropriate network interface depend routing metric configured networkconfiguration object multiple interface layer network method work expected linux weakhost model

minimumtransferrate mintransferrate mintransferrate interface specifying average minimum transfer rate file downloads file transfer fall rate terminated

maximumtransferrate long maximum transfer rate file downloads source data rate isnt direct control brightsign player download rate average specified value time

onlyrequestcache bool flag indicating player disconnect shortly beginning asset download player suitably configured proxy either globally assetpoolfetcherparams interface proxy continue download file making readily available assetfetching call future parameter true fileevent return response code accepted indicate success error reported usual progressevent final allfilescomplete event always eventallfailed download complete


## Authentication

interface contains authentication information downloading file

username string user name authentication

password string password authentication


## Header

interface contains list header pas file download entry list contains following parameter

value string header value


## MinTransferRate

value interface used calculate minimum transfer rate

bytespersecond transfer rate averaged periodinseconds file transfer terminated

periodinseconds time frame bytespersecond measurement averaged


note
note
transfer internet want periodinsseconds small number case network problem cause temporary drop performance large file transfer small bytespersecond limit averaging fifteen minute appropriate

developersdevelopersplayerapisjavascriptapisassetpoolmd
# assetpool

assetpool object represents directory storage device used store downloaded asset asset pool overview general information example

assetpool


interface assetpool
assetpoolstring poolpath
promisevoid protectassetsstring assetcollectionname assetlist asset
promisevoid unprotectassetsstring assetcollectionname
promisevoid reservestoragelong reservedstorageinbytes
promisevoid setmaximumpoolsizelong maximumpoolsizeinbytes
promiselong getpoolsize
promiseassetvalidationresult validateassetlist asset assetvalidationoptions option
promiseassetqueryresult queryfilesassetlist asset
promisebool areassetsreadyassetlist asset


interface assetinfo
attribute string name
attribute string link
optional attribute long size
optional attribute assethash hash
optional attribute string changehint
optional attribute assetfetchauthentication auth
optional attribute assetfetchheaders header


interface assethash
attribute string method
attribute string


interface assetfetchauthentication
optional attribute string user
optional attribute string password


interface assetfetchheaders


interface assetvalidationoptions
attribute deletecorrupt


interface assetqueryresult
attribute string name
attribute bool present


interface assetvalidationresult
attribute string name
attribute string reason



## Object Creation

create assetpool object first load brightsignassetpool module using require method create instance assetpool class string value specifying pool path must create assetpool instance pool path mean possible safely share single pool path brightscript javascript code


const assetpoolclass requirebrightsignassetpool
assetpool assetpoolclasssdpool


## AssetPool

interface perform operation asset pool

##### protectAssets()


promisevoid protectassetsstring assetcollectionname assetlist asset


request file asset pool protected deletion system software need prune file pool make space passed assetcollectionname used reference file protection need removed later using unprotectassets method protection affect assetpool instance object must protect asset care performing operation might prune file pool order sure asset still need pruned setting persistent beyond lifetime assetpool instance

##### unprotectAssets()


promisevoid unprotectassetsstring assetcollectionname


remove protection file protected passing corresponding assetcollectionname protectassets method

##### reserveStorage()


promisevoid reservestoragelong reservedstorageinbytes


operation assetpool instance assetpoolfetcher assetrealizer instance using attempt keep specified amount space free storage device containing pool file written storage device maximum size occupied pool reduced compensate setting stored persistently pool method must called time assetpool object created

##### setMaximumPoolSize()


promisevoid setmaximumpoolsizelong maximumpoolsizeinbytes


specifies maximum size asset pool method resourceintensive reservestorage useful creating multiple pool storage device ensure dont grow unevenly setting stored persistently pool method must called time assetpool object created

##### getPoolSize()


promiselong getpoolsize


return current size asset pool byte necessary walk pool directory structure looking every asset file slow access storage device recommended method called regularly production code

##### validate()


promiseassetvalidationresult validateassetlist asset assetvalidationoptions option


recalculates hash every file pool compare expected value passed assetlist mean every asset file need read entirety take long time slow access storage device method used detect storage file system corruption method return assetvalidationresult interface containing validation result file second parameter assetvalidationsoptions interface specifying validation option option currently supported indicates whether asset mismatched hash automatically deleted default behaviour leave asset file place

##### queryFiles()


promiseassetqueryresult queryfilesassetlist asset


determines whether specified file present asset pool method return assetqueryresult interface containing query result method normally useful debugging development

##### areAssetsReady()


promisebool areassetsreadyassetlist asset


return true every asset assetlist present asset pool

## AssetInfo 

interface represents single asset file pool pool asset subset following property

name string name used look asset file realized must valid filename without slash asset name must unique within asset collection different asset collection asset name refer asset pool different asset pool asset name stored pool refer asset name using asset collection

link string used assetpoolfetcher download file file uris supported

size long optional file length byte known

hash assethash optional hash interface specifying hash algorithm hash value file hash provided created automatically link changehint

changehint string optional arbitrary value used client specify file changed even hash value download remain mostly useful hash known provider asset collection tell content changed example mediarss feed often provide guid content

auth assetfetchauthentication optional assetfetchauthentication interface specifying credential downloading asset default credential inherited assetpoolfetcherjavascriptapisassetfetchermd instance used download asset

header assetfetchheaders optional default http header specified header property passed start method used asset header disabled particular asset setting property null useful particular subset asset retrieved somewhere else require authentication currently possible provided specific header single asset


## AssetHash

interface contains hash information file

method string hash algorithm accepted value include sha1 sha224 sha256 sha384 sha512 besha1 besha1 custom hash algorithm useful referring large asset stored remotely recommended

string hash value hexadecimal format


## AssetFetchAuthentication

interface contains authentication information downloading file

userstring optional user name authentication

password string optional password authentication


## AssetValidationOptions

interface contains validation option validate method

deletecorrupt flag specifying whether corrupt file deleted validation


## AssetQueryResult

interface returned queryfiles method entry list contains following parameter

name string name queried file

present bool flag indicating whether queried file exists asset pool


## AssetValidationResult

interface returned validate method entry list contains following parameter

name string name checked file

reason string explanation failed validation

developersdevelopersplayerapisjavascriptapisassetpoolfilesmd
# assetpoolfiles

assetpoolfiles object provides direct access file asset pool

assetrealizer


interface assetpoolfiles
assetpoolfilesassetpool pool assetlist asset
promisestring getpathstring assetname
promiseassetinfo getinfostring assetname
promisevoid movefileintopoolstring sourcefilename string destinationassetname



## Object Creation

create assetpoolfiles object first need create assetpool instance download file using assetpoolfetcher instance load brightsignassetrealizer module using require method create instance assetrealizer class using assetpool instance destination directory realization


const assetpoolclass requirebrightsignassetpool
assetpool assetpoolclasssdpool

const assetpoolfilesclass requirebrightsignassetpoolfiles
assetpoolfiles assetpoolfilesclassassetpool assetcollection


## AssetPoolFiles

interface gain access information file asset pool

##### getPath()


promisestring getpathstring assetname


return full path file pool corresponds named asset used read play execute corresponding asset required must modify file since change hash

##### getInfo()


promiseassetinfo getinfostring assetname


return assetinfo named asset present pool asset present returned promise rejected

##### moveFileIntoPool()


promisevoid movefileintopoolstring sourcefilename string destinationassetname


move existing file storage device pool pool asset corresponding name quick operation hash checked note method cause pruning asset already pool take place although cause subsequent operation prune pool method rarely useful

developersdevelopersplayerapisjavascriptapisassetrealizermd
# assetrealizer

assetrealizer object contains function realizing file extracting file asset pool placing standard file directory

assetrealizer


interface assetrealizer
constructorassetpool pool string destinationpath
promiseunsigned long long estimaterealizedsizeassetlist asset
promisevoid realizeassetlist asset
promisearrayvalidationresult validatefilesassetlist asset assetvalidationoptions option


interface assetvalidationoptions
attribute deletecorrupt


interface validationresult
attribute string name
attribute string reason



## Object Creation

create assetrealizer object first need create assetpool instance download file using assetpoolfetcher instance load brightsignassetrealizer module using require method create instance assetrealizer class using assetpool instance destination directory realization


const assetpoolclass requirebrightsignassetpool
assetpool assetpoolclasssdpool

const assetrealizerclass requirebrightsignassetrealizer
assetrealizer assetrealizerclassassetpool


## AssetRealizer

interface copy asset pool real named file file system perform related function

##### estimateRealizedSize()


promiseunsigned long long estimaterealizedsizeassetlist asset


return estimated amount space megabyte would taken file specified assetlistjavascriptapisassetpoolmd object realized

##### realize()


promisevoid realizeassetlist asset


place file destination directory specified passed assetlist object pool contain full required file method immediately fail file changed method attempt much work possible destructively modifying file system method automatically check length file hash match specified mismatch affected file deleted pool realization fails method cause unprotected asset pruned pool method indicates failure rejecting returned promise

note
pool destination must storage device file system

##### validateFiles()


promisearrayvalidationresult validatefilesassetlist asset assetvalidationoptions option


check hash every file passed assetlist corresponding file destination path return string list containing mismatched file name mapped reason operation take long time slow access storage device normally useful file system storage corruption suspected debugging option parameter string list currently support single option

deletecorrupt automatically deletes file match expected hash default file deleted


## ValidationResult

interface returned validatefiles method indicate result realize operation

name string name mismatched file realize operation fails

reason string explanation failed realize operation roassetrealizereventdevelopersbrightscriptobjectreferencecontentmanagementobjectsroassetrealizereventmd page list possible reason string

developersdevelopersplayerapisjavascriptapisaudiomd
# audio .

audio object javascript object ronodejs allows playback audio replicating functionality html5 audio element

audio


interface audio
error state
readonly attribute mediaerror error

network state
attribute string
readonly attribute string currentsrc
readonly attribute unsigned short networkstate
const unsigned short networkempty
const unsigned short networkidle
const unsigned short networkloading
const unsigned short networknosource

void load
string canplaytypestring type

ready state
readonly attribute unsigned short readystate
const unsigned short havenothing
const unsigned short havemetadata
const unsigned short havecurrentdata
const unsigned short havefuturedata
const unsigned short haveenoughdata

readonly attribute boolean seeking

playback state
attribute double currenttime
readonly attribute double duration
readonly attribute boolean paused
attribute double defaultplaybackrate
attribute double playbackrate
readonly attribute boolean ended
attribute boolean autoplay
attribute boolean loop
void play
void pause

void setsyncparamsstring domain string syncid string isotimestamp

control
attribute double volume
attribute boolean muted

brightsign extension
attribute string pcmaudio
attribute string compaudio

attribute xbsstreamtimeout
attribute string xbsaudiomode

present unimplemented
attribute string preload
readonly attribute timeranges buffered
readonly attribute double initialtime
readonly attribute date startoffsettime
attribute boolean control
readonly attribute timeranges played
readonly attribute timeranges seekable

readonly attribute texttrack track
mutabletexttrack addtrackstring kind optional string label optional string language




## Object Creation

create audio object first load brightsignaudio module using require method create instance audio class using following example


audioclass requirebrightsignaudio
audioplayer audioclass


## Audio

interface create audio object

### Event

seeked event fired medium loop back start

### Methods

##### load() 


void load


trigger processing load start playback point ready play first frame autoplay also start playback readystate networkstate altered multiple event fire playback start

##### canPlayType() 


string canplaytypestring type


return whether passed mime type displayed brightsign player

##### play() 


void play


start resume playback

##### pause() 


void pause


pause playback

##### setSyncParams()


void setsyncparamsstring domain string syncid string isotimestamp


brightsign extension documented

## Audio Parameters

string contains medium resource element file url supported currently including relative url current script file absolute filesystem path player returned reading value back always absolute file protocol front

currentsrc string contains medium resource element

networkstate unsigned short enum indicates current state fetching medium attribute move state selected playback begin support currently file dynamic used http possible value

networkempty

networkidle

networkloading

networknosource

readystate unsigned short indicates readiness state medium attribute move state selected playback begin possible value

havenothing

havemetadata

havecurrentdata

havefuturedata

haveenoughdata

seeking boolean indicates medium seeking position

currenttime double specifies current playback time second floating point currently seeking supported setting attribute effect playback completed return value duration

duration double specifies current duration medium second floating point

paused boolean reflects whether medium playback currently paused

defaultplaybackrate double cannot anything always return normal speed playback supported

playbackrate double cannot anything always return normal speed playback supported

ended boolean reflects medium playback reached medium

autoplay boolean indicates whether playback automatically begin medium available play without interruption

loop boolean set whether playback loop value used load called setting playback started effect

volume double control volume playback

muted boolean control muting unmuting audio

pcmaudio string route decoded audio output string output available analog earc output example usba0 multiple output specified using semicolon delimeter example earc analog

compaudio string route compressed audio direct earc without decoding earc

xbsstreamtimeout control timeouts streaming

xbsaudiomode string control downmix audio mono possible value monoleftmixdown monorightmixdown default stereo using audio player output single stereo output left channel right channel


## Unimplemented Methods and Properties

preload

buffered

initialtime

startoffsettime

control

played

seekable

track


## Examples


const audioclass requirebrightsignaudio
audioplayer audioclass
audioplayersrc storagesdfilemp4
audioplayervolume
audioplayerload
audioplayerplay



setupaudio audio setupobj
objectentriessetupobj
audiokey



interval setinterval 10000
const audioclass requirebrightsignaudio
audio audioclass
setting
storagesdfilemp4
autoplay true
loop false
volume
pcmaudio analog

setupaudioaudio setting
audioload
audioaddeventlistenerended
audiosrc
audio null
clearintervalinterval
processexit0



developersdevelopersplayerapisjavascriptapisaudioconfigmd
# audioconfig

object allows mixing leveling audio stream passed audio output

audioconfig


interface audioconfiguration
promiseaudioconfig getconfig
promisevoid applyconfigaudioconfig config


interface audioconfig
attribute string modename
optional attribute srcrate
optional attribute bool pcmonly
optional attribute bool autolevel



## Object Creation

create audioconfig object load brightsignaudioconfiguration module using require method


audioconfigurationclass requirebrightsignaudioconfiguration
audioconfig audioconfigurationclass


## AudioConfiguration

interface create audioconfig object

##### getConfig()


promiseaudioconfig getconfig


return audio configuration information

##### applyConfig()


promisevoid applyconfigaudioconfig config


configures audio mode switch dynamic prerouted

## AudioConfig

interface contains audio configuration parameter series product line note information product

modename string set audio routing mode

dynamic default mode mixing audio stream differing sampling rate cause playback fail differing volume level normalized audio stream cannot added output currently audio playing parameter associative array ignored however product line single audio stream played output time parameter associative array ignored

prerouted remove audio stream output currently audio playing additional audio routing behavior determined srcrate pcmonly autolevel parameter

srcrate optional set sample rate audio stream converted prerouted audio mode value either 44100 48000

pcmonly bool optional enables true disables false compressed audio support prerouted audio mode

autolevel bool optional enables disables volume leveling audio output prerouted audio mode setting enabled audio stream particular output play similar volume


note
audio configuration parameter definition specific series product
modename string set audio routing mode

dynamic default mode single audio stream played output time parameter associative array ignored

prerouted multiple audio stream played simultaneously analog earc output audio always sample rate converted value srcrate stream started stopped without affecting playing stream

srcrate optional set sample rate audio stream converted prerouted audio mode value 32000 96000

pcmonly bool optional feature available series product line

autolevel bool optional feature available series product line

## Example

example code get current audio configuration alters though doesnt check value changing writes back


audioconfigurationclass requirebrightsignaudioconfiguration
audioconfig audioconfigurationclass
configstate await audioconfiggetconfig
configstatemode prerouted
configstatesrcrate 48000
await audioconfigapplyconfigconfigstate


developersdevelopersplayerapisjavascriptapisaudiooutputmd
# audiooutput

object allows individual control audio output player

audiooutput


constructorstring outputname
interface audiooutput
attribute float volumelinear
attribute float volumedb
attribute long delay
attribute float treble
attribute float bass
attribute boolean mute
readonly attribute string name



## Object Creation

create audiooutput object require method

must also enter audiooutputclass example analog used audiooutputclass parameter take following string

none

hdmi hdmi1 hdmi2 hdmi3 hdmi4 series player multiple output



spdif

analog

analogn

earc au335

support multiple output using port naming terminology rodeviceinfogetusbtopologydevelopersbrightscriptobjectreferencesystemobjectsrodeviceinfomd



audiooutputclass requirebrightsignaudiooutput
audiooutput audiooutputclassanalog


## AudioOutput

interface create audiooutput object

volumelinear float set linear volume specified output percentage represented floating point number

volumedb float set volume decibel specified output percentage represented floating point number

delay long series player delay audio specific audio output lagging decoded sample reach output delay millisecond

treble float series player set treble specified output decibel treble floating point number range indicating modification audio signal

bass float series player set bass specified output decibel bass floating point number range indicating modification audio signal

mute boolean mute specified output true method false default

name string name output

plugstate boolean value true corresponding output plug false undefined plug state cannot determined current hardware version supported 90163 onwards

developersdevelopersplayerapisjavascriptapisbrightsignassetpoolbrightsignassetpoolexamplemd
# BrightSign Asset Pool Example

script show brightsign asset pool used javascript work nodejs chromium intended full application doesnt anything asset downloaded


license

copyright 2020 brightsign

permission hereby granted free charge person obtaining copy
software associated documentation file software deal
software without restriction including without limitation right
copy modify merge publish distribute sublicense andor sell
copy software permit person software
furnished subject following condition

copyright notice permission notice shall included
copy substantial portion software

software provided without warranty kind express
implied including limited warranty merchantability
fitness particular purpose noninfringement event shall
author copyright holder liable claim damage
liability whether action contract tort otherwise arising
connection software dealing
software

customise setting environment
const storagepath storagesd
const poolpath storagepath examplepool
const serverprefix

const requirefs
const assetpool requirebrightsignassetpool
const assetpoolfiles requirebrightsignassetpoolfiles
const assetfetcher requirebrightsignassetfetcher
const assetrealizer requirebrightsignassetrealizer

create asset collection array used rest
program asset collection usually come either directly
indirectly server somewhere rather generated
code like
function makeassetcollection

asset must name link everything else
optional property required
example osupdate property used
script
videoasset1
name brightlinkmp4
hash method sha256
82e5e800ff4b2608ae996b6c9fce78c0d84b82cba0da270251846324f48fb076
link serverprefix brightlink201minmp4rawtrue
size 17219989


videoasset2
name cmscontrolmp4
hash method sha512
d476296b114fda612917b1568a9f7ffe6f54f3f927b2d1ecc932816e912619eeef980e1adc16d8b1d7914d3f172cd6a2ef17172ea3251ddcdbb3d151faa6818f
link serverprefix cms2bcontrol20120minmp4rawtrue
size 5633877


dont want risk actually changing version
brightsign running example cript real
brightsignos file realized root
storage device fail find expected
header rename placeholderbsfwinvalid
osupdateasset
name placeholderbsfw
hash method sha1 20e89c9ba0491590e3c34bc704171c0c02e643c3
link serverprefix placeholderbsfwrawtrue
size
osupdate true


assetcollection
videoasset1
videoasset2
osupdateasset


return assetcollection


convert progress event useful string reporting
function progressstringevent

eventcurrentfiletotal undefined
size asset specified asset collection total size reported
fetch
return eventcurrentfiletransferredtostring unknown
else
return eventcurrentfiletransferredtostring eventcurrentfiletotaltostring
100eventcurrentfiletransferred eventcurrentfiletotaltofixed0



download asset arent already pool pool
whilst reporting progress
async function fetchassetsassetpool assetcollection

consolelogfetch jsonstringifyassetcollectionmapasset assetname

assetfetcher assetfetcherassetpool

assetfetcheraddeventlistenerfileevent event
called time fetcher finished trying
download asset whether successful
called asset already pool
consolelogasset eventindex 1tostring
eventfilename complete eventresponsecodetostring eventerror


assetfetcheraddeventlistenerprogressevent event
called approximately progress interval
specified option indicate
download
consolelogasset eventindex 1tostring eventtotaltostring eventfilename
progress progressstringevent


const fetchoptions
receive asset progress event every five second
progressinterval
download asset three time giving
fileretrycount
give fail download least 1024 byte
second period
minimumtransferrate bytespersecond 1024 periodinseconds



await assetfetcherstartassetcollection fetchoptions

catch
consolelogfetch failed errmessage
throwerr



order make asset pool need look
pool filename refer
async function useassetsassetpool assetcollection

file assetpoolfilesassetpool assetcollection

const filename brightlinkmp4 cmscontrolmp4
const path await filesgetpathfilename
consolelogasset filename path



file need appear filesystem outside pool
example brightsignos update file must written root
storage device found realizing copy file
slow large file
async function realizeassetsassetpool assetcollection

realizer assetrealizerassetpool storagepath

want realize file
const assetstorealize assetcollectionfilterasset assetosupdate
consolelogrealize jsonstringifyassetstorealizemapasset assetname
await realizerrealizeassetstorealize


function ensuredirectoryexistspath

fsmkdirsyncpath
catch

errcode eexist
throwerr



function exceptiontostringerr

instanceof error
return errname errmessage
else typeoferr string
return
else
return jsonstringifyerr


async function runexample

consolelogstart
ensuredirectoryexistspoolpath

assetpool instance created given pool
path multiple instance risk disagreeing
asset protected pruning
assetpool assetpoolpoolpath

dont pool grow larger 500mib
await assetpoolsetmaximumpoolsize500 1024 1024

dont free space storage device fall 100mib
await assetpoolreservestorage100 1024 1024

const assetcollection makeassetcollection

need stop fetcher pruning asset
currently care order make space fetching
asset realizing existing one asset protected
assetpool instance destroyed unprotectassets
called name
await assetpoolprotectassetscollection1 assetcollection

await fetchassetsassetpool assetcollection

case failure fetch asset cause
fetchassets thrown exception wont
however larger script convenient
call areassetsready determine whether asset collection
ready
await assetpoolareassetsreadyassetcollection
await useassetsassetpool assetcollection
await realizeassetsassetpool assetcollection
else
consolelogassets downloaded successfully



runexample

consolelogcomplete
processexit0

catcherr
consolelogfailed exceptiontostringerr
processexit1



developersdevelopersplayerapisjavascriptapisbrightsignassetpoolbrightsignassetpoolmd
# BrightSign Asset Pool



table content

core conceptscoreconcepts
managing pool sizemanagingpoolsize
referring asset poolreferringtoassetsinthepool
hash uniquenesshashuniqueness
asset metadataassetmetadata
hashinghashing
usage overviewusageoverview
exampleexample

brightsign asset pool provides reliable resilient mechanism downloading storing retrieving medium asset file required player presentation

## Core Concepts

### The Pool

asset pool directory hierarchy single root directory often simply named pool underlying implementation require asset stored number subdirectory improve performance simple filesystems like

destination particular asset pool determined hash digest content case hash metadata make contentaddressable store order refer asset either downloaded necessary know hash similar object stored repository

pool configured maximum size andor ensure particular amount space remains free storage device contains order stop pool growing beyond bound file pruned file must pruned must protected operation started write pool

asset stored pool using particular hash stored pruned request download asset already pool immediately succeed since asset already present mean switching presentation share asset even perhaps one havent used avoid downloading asset unnecessarily

### Asset Collections

asset collection list asset metadata metadata either directly contains hash specific field hash generated directly field metadata also provides name asset allows asset therefore file pool looked name asset collection necessary provide meaning asset stored pool asset collection exist memory stored pool

### Synchronization Specification

synchronization specification often refered sync spec consist formatted json used generate asset collection also space extra information useful downloading asset recommended unless compatibility existing system required

### Asset Fetcher

asset fetcher run asynchronously downloading asset mentioned asset collection currently available pool file content automatically verified supplied hash download

#### Protocols

asset expected primarily downloaded using http http however fetcher also support file url

#### Authentication

arbitrary http header provided fetching asset asset collection fetcher support http basic digest ntlm authentication individual asset within collection marked opting providing header authentication

## Managing Pool Size

pool intended live long time asset fetched required pool becomes full unused asset pruned make space mean asset still required required must protected performing operation prune fetching realizing

pool size restricted way

requiring certain amount space storage device always kept free mean space reserved log grow pool operation prune ensure least requested amount space remains free checking amount free space storage device lightweight operation method preferred

setting maximum size pool occupy used combination previous method attempting exceed either threshold trigger pruning calculating size pool requires adding size file individually first operation take longer usual first calculation complete pool size updated based modification pool subsequent operation less overhead


file considered pruning based long last fetched would fetched already present pool leastrecently fetched unprotected file pruned first note unless working asset close maximum size pool often mean failure protect asset effect

## Referring To Assets In The Pool

asset file often used directly pool pool filename corresponding asset looked name asset collection

sometimes necessary asset file appear name within filesystem asset file copied destination directory known realization used necessary since slow alternatively asset collection made appear virtual filesystem

## Hash Uniqueness

hash particular asset file must unique happens automatically normal hash algorithm sha256 since hash collision possible file different content generate hash known hash collision older hash algorithm sha1 known hash collision occur file deliberately constructed create collision occur accident

sometimes actual hash asset available prior download case part asset metadata change hint hashed together instead asset change part metadata must also change asset fetcher know download asset

possible http header like etag lastmodified part hash since arent known prior download change independently

## Asset Metadata

description

name relative filename contain slash file realized asset name must unique within asset collection expected different asset collection contain asset name asset name stored pool asset file pool referenced multiple name even within asset collection
size file length byte
hash hash algorithm hash file content
link source
changehint arbitrary value used client ensure file hash considered identical unless value also match
auth specify extra authentication information
probe medium probe data useful cheetah panther
pattern wildcard pattern match

## Hashing

### Simple Hash Algorithms

sha1 sha224 sha256 sha384 sha512

### BESHA1 Algorithm

algorithm useful referring remote content large download authoring recommended

### No Hash

hash specified hash generated internally hashing together link changehint field

## Usage Overview

brightsign asset pool used brightscript javascript possible share single pool across however brightscript rohtmlwidgetmapfilefromassetpool method used make particular asset collection appear file particular prefix

### BrightScript



### Javascript

create brightsignassetpool object represent asset pool passing path pool directory

create asset collection data structure javascript array object containing metadata asset wish

protect asset calling assetpoolprotectassets method stop deleted order make space

create brightsignassetfetcher object passing pool

call assetfetcherstart method passing asset collection asset present pool start downloaded

progress monitored adding handler progressevent fileevent event

fetch attempt completes successfully promise returned assetfetcherstart resolved least asset could fully downloaded promise rejected

promise returned assetfetcherstart resolve fetch attempt complete

create asset javascript array object containing metadata

create brightsignassetfiles object passing pool asset collectionthis object used retrieve full path file pool correspond asset name specified assetpoolfiles information

create brightsignassetrealizer object passing pool call realize method wish copy asset pool directory using asset name note slow recommended file must exist filesystem brightsignos upgrade file bsfw

create brightsignassetcollectionview object passing pool asset collection create virtual storage device containing asset using name directory structure asset collection assetpoolfiles information


## Example

brightsign asset pool example show asset pool used javascript work nodejs chromium brightsign shell follows


node bsassetpoolexamplejs


developersdevelopersplayerapisjavascriptapiscecmd
# cec

object let send message consumer electronics control




interface receiveevent
attribute string type
attribute arraybyte data


callback receiveeventcallback void receiveevent event

interface
promisevoid sendarraybyte data
void addeventlistenerstring type receiveeventcallback callback
void removeeventlistenerstring type receiveeventcallback callback



## Object Creation

create object load brightsigncec module using require method


const cecclass requirebrightsigncec
const cecclass


specific hdmi port player output follows


const cecclass requirebrightsigncec
const cecclasshdmi2 modify hdmi1 hdmi2 hdmi3 hdmi4 needed


## Cec

### Event

receiveevent reception path implemented receive event receive message generic field

type event type receive

data arraybyte frame


### Method

##### send()


promisevoid sendarraybyte data


sends message

data arraybyte frame


##### port\_name ()


promisevoid


parameter optional argument

default default output platform normally hdmi1

hdmix number number hdmi output platform

earc default au335


note
note
brightsignos 8255 implementation series product reply message correct data without involving script
cecmsggetcecversion

cecmsgabort

cecmsggivedevicepowerstatus

cecmsggiveosdname

cecmsggivedevicevendorid

cecmsggivefeatures

cecmsggivephysicaladdr

cecmsgusercontrolpressed

cecmsgusercontrolreleased

cecmsgreportphysicaladdr

## Example

following example send receive message bscectransmitterplayerapisbrightscriptjavascriptobjectsbscectransmittermd example turn display


const cecclass requirebrightsigncec
const cecclass

initiatoraddress 0x40
opcodegetversion 0x9f
opcodeversion 0x9e
version

function onrxeventpacket
frame packetdata
opcode frame1
consolelogframe opcode opcode
consolelogjsonstringifyframe
opcode opcodeversion
version frame2tostring16
consolelogversion version



function cecversion
return promiseasync resolve
version
buffer
buffer0 initiatoraddress
buffer1 opcodegetversion
cecsendbuffer
thenasync function
await async promiseresolve settimeoutresolve 1000
consolelogversion received version
resolve

catch functionerror
consolelogooops error
resolve




async function runtest
cecaddeventlistenerreceive onrxevent
await cecversion



developersdevelopersplayerapisjavascriptapiscompositormd
# compositor

compositor object allows perform action related video compositor

compositor


interface compositor
void pauseint timeoutms
void resume
getcrc



## Object Creation

create compositor object first load brightsigncompositor module using require method create instance screenshot class


compositorclass requirebrightsigncompositor
compositor compositorclass


## Compositor

##### pause()


void pauseint timeoutms


suspends graphic compositor update specified number millisecond resume method called maximum interval second graphic compositor paused visual element updated except videodevelopershtmldevelopmenthtmlvideomd scrolling tickersdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrotextwidgetmd offscreen chromium texture method combine intensive graphic layout operation single vsync update

##### resume()


void resume


resume graphic compositor paused pause method

##### getCrc()


getcrc


return signal single integer method allows script compare moment graphic output return value differ output identical

developersdevelopersplayerapisjavascriptapisconfigurednetworksmd
# configurednetworks

configurednetworks object provides array persistent configuration name even active present configuration accessed using brightsignnetworkconfiguration object

configurednetworks


interface configurednetworks
promisearraystring getconfigurationnames



## Object Creation

create configurednetworks object load brightsignconfigurednetworks module using require method


configurednetworksclass requirebrightsignconfigurednetworks
configurednetworks configurednetworksclass


## ConfiguredNetworks

##### getConfigurationNames()


promisearraystring getconfigurationnames


method return array persistent configuration name even active present

developersdevelopersplayerapisjavascriptapiscontrolportmd
# controlport

controlport object used configure output level connector monitor input provides support bp200bp900 button board gpio port typically led button attached gpio connector brightsign player brightsign expansion module

controlport


constructorstring port
interface controlport
bool setoutputvalueunsigned param
bool setoutputvaluesunsigned unsigned unsigned unsigned
bool setpinvalueunsigned unsigned param
bool getpinvalueunsigned
bool configureasinputunsigned
bool configureasoutputunsigned
void close



## Object Creation

create controlport object require method


controlportclass requirebrightsignlegacycontrolport
controlport controlportclasstouchboard0gpio


controlport object created parameter specifies port used touchboard0gpio example port parameter following

brightsign specifies onboard gpio connector including gpio12 button

expandergpio specifies db25 connector brightsign expansion module brightsign expansion module attached object creation fail invalid returned

expanderngpio specifies usbtogpio device connected player multiple usbtogpio device controlled using separate rocontrolport instance first device corresponds expander0gpio second expander1gpio

expanderdip specifies eight switch brightsign expansion module brightsign expansion module attached object creation fail invalid returned note plugging brightsign expansion module supported

touchboardngpio retrieves event specified bp200bp900 button board event handled manner event brightsign port

touchboardnledsetup set various output option specified bp200bp900 button board

touchboardnled set bit button specified bp200bp900 button board bit indicate whether associated


note
since multiple bp200bp900 button board connected player simultaneously value specifies port enumeration board ordering multiple attached board dependent order appear data structure returned rodeviceinfogetusbtopologydevelopersbrightscriptobjectreferencesystemobjectsrodeviceinfomd unspecified enumeration value synonymous button board enumeration value touchboardgpio touchboard0gpio identical

## ControlPort

##### SetOutputValue()


bool setoutputvalueunsigned param


specifies desired state output attached control port bit integer

##### SetOutputValues()


bool setoutputvaluesunsigned unsigned unsigned unsigned


configures button bp200bp900 button board method used controlport object instantiated touchboardnledsetup touchboardnled parameter bp200bp900 setup detail

parameter integer value

##### SetPinValue()


bool setpinvalueunsigned unsigned param


return bool configures either

output specified gpio button value either button configured output resulting level undefined example setpinvalue01 setpinvalue11 setpinvalue21 setpinvalue31

output behavior bp200b900 button board case offset value bitmask unsigned parameter


##### bool GetPinValue()

return true specified input active return false inactive connected high

##### bool ConfigureAsInput()


bool configureasinputunsigned


mark specified button input invalid button number passed false returned successful function return true input button tristated driven high externally

##### bool ConfigureAsOutput()


bool configureasoutputunsigned


mark specified button output invalid button number passed false returned successful function return true output driven high depending current output state page table pin corresponding button onboard gpio connector

##### Close()


void close


shuts controlport instance

## Events

addeventlistenerjavascriptapisjavascripteventhandlingmd listen controldown controlup controlevent

## Example

example script set bp900 twinkle turning button different point cycle


const controlportclass requirebrightsignlegacycontrolport
const controlportclasstouchboard0led
const ledsetup controlportclasstouchboard0ledsetup

ledsetupsetpinvalue0 0x000b00a0

ledsetpinvalue0 0x07fe
ledsetpinvalue1 0x07fd
ledsetpinvalue2 0x07fb
ledsetpinvalue3 0x07f7
ledsetpinvalue4 0x07ef
ledsetpinvalue5 0x07df
ledsetpinvalue6 0x07bf
ledsetpinvalue7 0x077f
ledsetpinvalue8 0x06ff
ledsetpinvalue9 0x05ff
ledsetpinvalue10 0x03ff


developersdevelopersplayerapisjavascriptapiscookiestoremd
# cookiestore

cookiestore object retrieves list cooky containing browser implies class available code running inside browser instance ronodejs

cookiestore


interface cookie
attribute string domain
attribute string path
attribute string name
attribute string value


interface cookiestore
arraycookie getcookies



## Object Creation


cookiestoreclass requirebrightsigncookiestore
cookiestore cookiestoreclass


## Cookie

##### getCookies()


arraycookie getcookies


get cooky containing browser

domain string specifies host allowed receive cookie including subdomains

path string send cookie header path must exist request

name string name cookie

value string value cookie


## Example

list cooky saved browser instance console


cookiestoreclass requirebrightsigncookiestore
cookiestore cookiestoreclass

cooky cookiestoregetcookies

cookiesforeachcookie consolelogcookie domain cookiedomain cookie path cookiepath cookie name cookiename cookie value cookievalue


developersdevelopersplayerapisjavascriptapisdecoderconfigurationmd
# decoderconfiguration

decoderconfiguration object allows configure video decoder mosaic mode

decoderconfiguration


interface decoderconfiguration
promisedecoderconfigread getconfig
promisevoid applyconfigdecoderconfig config


interface decoderconfigwritable
attribute string name
attribute string friendlyname
attribute string configuredsize
attribute zindex
attribute bool mosaicdeinterlace


interface decoderconfig decoderconfigwritable
attribute string maxsize
attribute string mode
attribute usagecount
attribute maxusage



## Object Creation

create decoderconfiguration object first load brightsigndecoderconfiguration module using require method create instance decoderconfiguration class


decoderconfigurationclass requirebrightsigndecoderconfiguration
decoderconfig decoderconfigurationclass


## DecoderConfiguration

interface retrieve modify video decoder data

##### getConfig()


promise decoderconfigarray getconfig


return array decoderconfig interface interface describes video decoder

##### applyConfig()


promise void applyconfigdecoderconfigarray config


configures video decoder either standard mode mosaic mode standard mode single decoder used play single video mosaic mode decoder used decode multiple video different local remote source method accepts array decoderconfig interfacesattributes readonly maxsize ignored

system software selects video decoder based resolution probed video file standard mode attempt select decoder closest maximum supported resolution 1920x1080 decoder 3840x2160 decoder without exceeding maximum resolution decoder configured mosaic mode match video resolution specified configuredsize instead decoder support maximum resolution select decoder manually using friendlyname attribute

select decoder html video include decoderfriendlyname property attributedevelopershtmldevelopmenthtmlvideomd


video decodermainvideo video
video decodersdvideo video


maxusage value decoder determines many video player assigned decoder using system software algorithm described abovevideo player beyond maxusage limit assigned another decoder displayed hand manually assign video player using friendlyname decoder assign video player decoder maxusage limit cause unpredictable videodisplay behavior

## DecoderConfig

interface contains setting video decoder contains editable readonly attribute

### Editable

name string system name video decoder decoder availability differs model

primary decoder xtx44 model

secondary decoder xtx44 model

sole decoder hdx24 xtx43 4kx42 xdx34 xdx33 model

first decoder

second decoder

friendlyname string name referencing decoder html brightscript

configuredsize string maximum resolution decoder accept framerates resolution decoder maximum resolution limit decoder standard mode otherwise mosaic mode

3840x2160

1920x1080

720x576

352x288

qcif 176x144


caution
important
upscaling video mosaic mode currently cause severe performance degradation

zindex zindex video window standard mode group video window mosaic mode relative graphic plane

video window group window positioned front graphic plane

video window group window positioned behind graphic plane

mosaicdeinterlace bool flag indicating whether mosaicmode video interlaced enabling deinterlacer allow playback interlaced video mosaic mode reduce number mosaicmode video decoded simultaneously well


### Read-Only

maxsize string maximum resolution decoder system software value either

mode string current mode decoder either regular mosaic

usagecount number video currently decoded decoder

maxusage maximum number video decoded simultaneously decoder value always regular mode optimum maxusage limit described limit lower depending number factor including interlacing frame rate

decoder

video

video

video

video

qcif video

decoder

video

video

video

video

qcif video


## Example

script retrieves current video decoder configuration modifies decoder used decode video


decoderconfigurationclass requirebrightsigndecoderconfiguration
decoderconfig decoderconfigurationclass

function finddecoderelement
return elementname


function setdecoderdecoderlist
decoder decoderlistfindfinddecoder
decoderfriendlyname mainvideo
decoderconfiguredsize
decoderzindex
decoderconfigapplyconfigdecoderlistthen
catch
functiondata
consolelogjsonstringifydata



decoderconfiggetconfigthen
functiondata
setdecoderdata

catch
functiondata
consolelogjsonstringifydata



developersdevelopersplayerapisjavascriptapisdevicecustomizationmd
# devicecustomization

object provides method encrypt storage released version 90146

devicecustomization


interface devicecustomization
promisevoid encryptstoragestring device storageencryptionoptions params


interface storageencryptionoptions
attribute string method
attribute string passphrase
attribute boolean format



## Object Creation


devicecustomizationclass requirebrightsigndevicecustomization
devicecustomization devicecustomizationclass


## DeviceCustomization

##### encryptStorage()


promisevoid encryptstoragestring device storageencryptionoptions params


encrypts content storage device using encryption stored private section player registry prevents device reading name content file storage device though file metadata still readable storage device still mounted device list delete copy file even though cannot read

device parameter specifies storage drive encrypt example storagesd storageusb1 storagessd process configured passed storageencryptionoptions parameter

## StorageEncryptionOptions

##### Attributes

method string encryption method following

none encryption disabled encryption key storage device deleted registry

passphrase storage device encrypted using unobfuscated passphrase

obfuscatedpassphrase storage device encrypted using obfuscated passphrase contact supportbrightsignbizmailtosupportbrightsignbiz learn generating obfuscation storing player

brightsignkey storage device encrypted using encryption common brightsign player shared outside party

generatekey storage device encrypted using encryption generated ondemand using secure random generator private registry player contains copy value registry erased becomes corrupted recover data storage device private registry distinguish different physical volume drive example encrypt card first card overwritten second card encrypted case randomly generated data first card irretrievable

passphrase string passphrase encrypting storage device parameter must included method specified passphrase obfuscatedpassphrase

format boolean setting parameter true cause specified storage device reformattedall existing file deleted guaranteed securely erased device encrypted however device cannot reformatted operation fail parameter false storage device mounted previously encrypted using supplied

storage device hasnt previously encrypted encrypted leaving preexisting file unencrypted storage device encrypted using different operation fail

format parameter specified storage device mounted previously encrypted using supplied storage device hasnt previously encrypted operation fail

developersdevelopersplayerapisjavascriptapisdeviceinfomd
# deviceinfo

deviceinfo object let identify device hardware firmware feature

deviceinfo


interface deviceinfo
attribute string model
attribute string osversion
attribute string bootversion
attribute string serialnumber
attribute string family

osversioncomparestring version
bootversioncomparestring bootversion
bool osversionisatleaststring version
bool bootversionisatleaststring bootversion
bool hasfeaturestring feature
promise string getloadstatisticsstring item
promise temperaturelocation gettemperature
promise usbtopologyinterface getusbtopology


dictionary temperaturelocation
float celsius


interface usbtopologyinterface
attribute string
attribute string
attribute string
attribute string
optional attribute string category
optional attribute string ident
attribute arrayusbtopologyinterface child




## Object Creation

create deviceinfo object load brightsigndeviceinfo module using require method


diclass requirebrightsigndeviceinfo
diclass



## DeviceInfo

##### getLoadStatistics()


promise string getloadstatisticsstring item


provides current performance information related linux kernel item following

loadavg provides information system performance first three column measure utilization past minute respectively fourth column display number currently running process total number process last column display recently used process

meminfo display physical swap memory usage

slabinfo provides information memory usage slab level

stat provides overall statistic system example number page fault since system booted

vmstat display detailed virtual memory statistic kernel

zoneinfo provides overall statistic system broken system node

interrupt display interrupt many type

version provides kernel version


##### getTemperature()


temperaturelocation gettemperature


return

string dynamic string location

value float device temperature floating point value


##### getUsbTopology()


usbtopologyinterface getusbtopology


get topology player

attribute return information brightsign player

model string return model name brightsign device running script string example hd1020 xd230

osversion string return version number brightsign device running script

bootversion string return version number brightsign boot firmware also known safe mode string example

serialnumber string return device serial number empty string unique unit running script

family string return single string indicates family device belongs device family model capable running firmware


##### osVersionCompare()


osversioncomparestring version


function return integer greater zero current version greater parameter exactly equal less zero lesser example


diosversioncompare82 consolelogfirmware version greater





diosversioncompare84 consolelogfirmware version less


##### bootVersionCompare()


bootversioncomparestring bootversion


function return integer greater zero current boot loader version greater parameter exactly equal less zero lesser example osversioncompare

##### osVersionIsAtLeast()


bool osversionisatleaststring version


return true brightsign version device greater equal version number represented passed string example 4013

##### bootVersionIsAtLeast()


bool bootversionisatleaststring bootversion


return true brightsign boot version device greater equal version number represented passed string example 4422

##### hasFeature()


bool hasfeaturestring feature


return true player feature passed string passed caseinsensitive string parameter present current device firmware possible feature queried script listed

caution
important
pas parameter listed return false even feature available hardware firmware

serial serial port

audio1 first audio output

audio2 second audio output

audio3 third audio output

brightscript1 brightscript version

brightscript2 brightscript version

component video component video output

ethernet ethernet interface

gpio connector da15 pheonixstyle gpio port

hdmi hdmi output

hdmi input hdmi input

hevcdecode h265 video decoder

mediadecryption ability decrypt aesencrypted medium including video image audio file

nand storage nand storage boot loader firmware

networking form networking capability false return indicate network currently available

reset button reset button

registry onboard persistent storage

realtime clock

sdhccompatible storage

sdhc sdhccompatible storage

serial port first serial port

serial port second serial port

serial port third serial port

button service button passing legacy term gpio12 button yield result

interface

output

videoencoder video encodertranscoder

## TemperatureLocation

celsius float return temperature device celsius floating point number


## UsbTopologyInterface

attribute return topology player used determine whether certain device connected certain port

string four character string encoding vendor product hexadecimal leading zero present alpha character lower case example 0b95

string four character string encoding vendor product hexadecimal leading zero present alpha character lower case example 0b95

string internal linux device node

stringports device connected include friendly value used determine physical port device connected player rodeviceinfo information

category string optional optional string describes device type example serial audio

ident string optional additional identifier device category ident system network interface name example usb0

child arrayusbtopologyinterface optional child present device category child device structure nested hub produce nested child data


## Example

example return topology device


diclass requirebrightsigndeviceinfo
diclass

usbtopology await digetusbtopology

parsetopology functionusbt
fori usbt
device usbti
devicecategory
parsetopologydevicechildren
devicecategory
consolelogfound devicefid interface deviceident



parsetopologyusbtopology


replace bsdeviceinfo deviceinfo object


typeofbsdeviceinfo typeof undefined

globalbsdeviceinfo class bsdeviceinfo
constructor
requirefs
deviceinfoclass requirebrightsigndeviceinfo
deviceinfo deviceinfoclass

property getters
thismodel deviceinfomodel
thisversion deviceinfoosversion
thisbootversion deviceinfobootversion
thisdeviceuniqueid deviceinfoserialnumber
thisfamily deviceinfofamily
objectdefinepropertythis deviceuptime
objectgetownpropertydescriptordeviceinfo deviceuptimeget
enumerable true

method
thisversioncompare deviceinfoosversioncompare
thisbootversioncompare deviceinfobootversioncompare
thisfirmwareisatleast deviceinfoosversionisatleast
thisbootfirmwareisatleast deviceinfobootversionisatleast
thishasfeature deviceinfohasfeature
thisgetloadstatistics function
stats zoneinfo loadavg meminfo stat vmstat interrupt version boardid
result
statshass
result fsreadfilesyncproc stostring

return result

gettemperature getusbtopology present bsdeviceinfo class





developersdevelopersplayerapisjavascriptapisdevicestatusmd
# devicestatus

object provides information device hardware firmware feature

devicestatus


interface devicestatus
promisebvninformationlist getbvnpipelines
promisebvninformationlist getbvncomponents
promisepowerinformation getpowerstatus
promiseextensionsinformationlist getextensions
promisepoeinformation getpoestatus


interface powerinformation
attribute string source
attribute string switchmode
attribute string battery
attribute socpercent


interface bvninformation
attribute string name
attribute index
attribute bvnregisterlist register
attribute bvnpipelinelist item optional


interface bvnregister
attribute string name
attribute offset


interface bvnpipeline
attribute string name


interface extensionsinformation
attribute string name
attribute size optional
attribute string


interface poepowerinformation
attribute float value
attribute string unit


interface poeinformation
attribute string status
attribute poepowerinformation power optional



## Object Creation

create devicestatus object load brightsignstatus module using require method


devicestatusclass requirebrightsigndevicestatus
devicestatus devicestatusclass


## devicestatus

##### getPowerStatus()


promisepowerinformation getpowerstatus


return device battery status charging discharging complete absent fault

##### getExtensions()


promiseextensionsinformationlist getextensions


return promise yield object containing extension array element containing least name field field also present relied

##### getPOEStatus()


promisepoeinformation getpoestatus


return information whether power ethernet network supported available andor active device

## Powerinformation

source string possible value battery ethernet

switchmode string return soft hard

battery string possible value charging discharging complete absent fault

socpercent state charge battery percent empty full


## Extensionsinformation

name string name extension

size extension return size others player eac3 license installed report extension size included


## POEpowerinformation

value float return power value

unit string return power value unit


## POEinformation

status string status string active standby inactive

power poepowerinformation poepowerinformation detail


## Example

power status device


devicestatusclass requirebrightsigndevicestatus
devicestatus devicestatusclass

devicestatusgetpowerstatusthen
functiondata
consolelogjsonstringifydata

catch
functiondata
consolelogerror data



developersdevelopersplayerapisjavascriptapisdwsconfigurationmd
# dwsconfiguration

dwsconfiguration object allows configure diagnostic server player default diagnostic server enabled port player serial number password username always admin

dwsconfiguration



garbagecollected
interface
dwsconfig defaultconfig
promisedwsconfig getconfig
promisedwsresult applyconfigdwsconfigwritable config


interface dwsconfig
attribute port
attribute password password
attribute arraystring authenticationlist


interface dwsconfigwritable dwsconfig
attribute password password


interface password
attribute string value
attribute bool obfuscated


interface dwsresult
attribute bool restartrequired



## Object Creation

create dwsconfiguration object first load brightsigndwsconfiguration module using require method create instance dwsconfiguration class


dwsconfigurationclass requirebrightsigndwsconfiguration
dwsconfig dwsconfigurationclass


## DWS

interface retrieve modify configuration

##### getConfig()


promise dwsconfig getconfig


return dwsconfig interface containing current dwsconfiguration information password getconfig return true password parameter isnt password password getconfig return false password parameter

##### applyConfig()


promise dwsresult applyconfigdwsconfigwritable config


applies dwsconfiguration setting player method accepts dwsconfig interface return dwsresult interface indicates whether reboot required change take effect caller responsible requesting reboot restartrequired property dwsresult indicates whether reboot required

config parameter contain complete desired configuration previous configuration overwritten wish change item keeping rest configuration call getconfig modify returned object example example section

## DWSConfig

interface contains configuration parameter

port port number located address player default port setting value disable

password password password interface containing password setting enable without password protection value empty string obfuscated false

authenticationlist arraystring authentication scheme password entry currently accepts single value following accepted value

basic password validated using basic authentication

digest password validated using digest access authentication


note
note
enable without password authentication passwordvalue empty string passwordobfuscated false calling applyconfig method

## DWSConfigWritable

password password password interface containing password setting


## Password

interface contains password setting

value string password

obfuscated bool flag indicating whether password string obfuscated contact supportbrightsignbizmailtosupportbrightsignbiz learn generating obfuscation storing player


## DWSResult

interface contains result applyconfig operation

restartrequired bool flag indicating whether reboot required change effect script must perform reboot


## Examples


dwsconfigurationclass requirebrightsigndwsconfiguration
dwsconfig dwsconfigurationclass

configdata


configdataport 1010
configdatapassword
configdataauthenticationlist basic

pwvalue password
pwobfuscated false

dwsconfigapplyconfigconfigdatathen
functiondata
consolelogjsonstringifydata

catch
functiondata
consolelogjsonstringifydata

dwsconfiggetconfigthen
functiondata
consolelogjsonstringifydata

catch
functiondata
consolelogjsonstringifydata



change item keeping rest configuration call getconfig modify returned object


dwsconfigurationclass requirebrightsigndwsconfiguration
dwsconfig dwsconfigurationclass

dwsconfiggetconfig
thenfunctionconfig
pwvalue password
pwobfuscated false
configpassword
dwsconfigapplyconfigconfig

thenfunction
consolelogsuccess

catchfunctionerror
consolelogjsonstringifyerror



developersdevelopersplayerapisjavascriptapisfilesysteminfilemd
# filesysteminfile

filesysteminfile allows create update filesystems storage device

filesysteminfile


interface filesysteminfile
constructorstring path
promisestring getfilename
promiselong long getsize
promisevoid formatstring filesystem
promisevoid mount
promisevoid unmount



## Object Creation

create filesysteminfile object load brightsignfilesysteminfile module using nodejs require method


filesysteminfile requirebrightsignfilesysteminfile
fsif filesysteminfilestoragesdusbstoreimg node native create file


## filesysteminfile

interface configure filesysteminfile

##### getFilename()


promisestring getfilename


get name file used create filesysteminfile

##### getSize()


promiselong long getsize


retrieves size byte filesystem file used create filesysteminfile class

##### format()


promisevoid formatstring filesystem


creates specified filesystem file already exists supported filesystem type exfat

##### mount()


promisestring mount


mount filesystem need format filesystem already exists formatted

return string filepath return value path filesystem mounted cannot mounted

##### unmount()


promisevoid unmount


unmounts filesystem

## Example

example creates file system format mount unmounts using package


const requirefs
const filesysteminfile requirebrightsignfilesysteminfile

fsif


open
thenfunctionfiledescriptor
filedescriptor
return writefd

thenfunctionbytes
consolelogbytes written file
return closefd

thenfunction
create filesysteminfile using backing file
fsif filesysteminfilestoragesdusbstore

return format

thenfunction
return mount

thenfunction
actually stuff mounted filesystem

unmount mounted file second
settimeoutfunction
return unmount
10000

catchfunctionerror
consolelogjsonstringifyerror



create writable file file system
function open
return promisefunctionresolve reject
fsopenstoragesdusbstore functionerror
error rejecterror
resolvefd




write buffer allocating disk space file
function writefd
return promisefunctionresolve reject
fswritefd bufferalloc1 102410241024 functionerror byteswritten
error rejecterror
resolvebyteswritten




close created file
function closefd
return promisefunctionresolve reject
fsclosefd functionerror
error rejecterror
resolve




format file system
function format
return promisefunctionresolve reject
fsifformatexfat
thenfunction
consolelogfilesystem formatted
resolve

catchfunctionerror
rejecterror





mount filesystem internally
function mount
return promisefunctionresolve reject
fsifmount
thenfunctionmountpoint
consolelogfilesystem mounted mountpoint
resolve

catchfunctionerror
rejecterror




unmount filesystem internal mount point unmount mounted file
function unmount
return promisefunctionresolve reject
fsifunmount
thenfunction
consolelogfilesystem unmounted
resolve

catchfunctionerror
rejecterror





also reference public github example us brightsign device filesystem

developersdevelopersplayerapisjavascriptapisfilesysteminfomd
# filesysteminfo

filesysteminfo object provides information file system storage device connected player retrieve information storage device storageinfo object

filesysteminfo



constructorstring path string type
interface filesysteminfo
promisebool isreadonly
promisestring getfilesystemtype
promisefilesystemstats getstatistics


interface filesystemstats
attribute number blocksize
attribute number sizebytes
attribute number bytesfree
attribute number filesused
attribute number filesfree
attribute bool isreadonly



## Object Creation

create filesysteminfo object first load brightsignfilesysteminfo module using require method create instance filesysteminfo class string value specifying storage path


filesysteminfoclass requirebrightsignfilesysteminfo
filesysteminfo filesysteminfoclassstoragesd


following string value specify different storage drive

storageusb1 drive storage device connected player

storagesd primary microsd drive player

storagesd2 internal microsd drive player 4kx42 xdx32 model

storagessd internal player xtx44 xtx43 xdx34 xdx33 model


## FilesystemInfo

interface retrieve information file system

##### isReadOnly()


promisebool isreadonly


return boolean value indicating whether filesystem readonly

##### getFilesystemType()


promise domstring getfilesystemtype


return filesystem type whether encrypted ecryptfs following potential value

exfat

ext3

ext4

fat12

fat16

fat32



hfsplus

ntfs

ecryptfs version 901451


##### getStatistics()


promisefilesystemstats getstatistics


return filesystemstats interface containing information filesystem method take significant amount time return promise

## FilesystemStats

interface contains information filesystem

blocksize number size native block

sizebytes number amount total space

bytesfree number amount free space

filesused number number used inodes

filesfree number number free inodes

isreadonly bool flag indicating whether filesystem readonly


## Example


filesysteminfoclass requirebrightsignfilesysteminfo
filesysteminfo filesysteminfoclassstoragesd

filesysteminfogetfilesystemtypethen
functiondata
consolelogjsonstringifydata

catch
functiondata
consolelogjsonstringifydata


filesysteminfogetstatisticsthen
functiondata
consolelogjsonstringifydata

catch
functiondata
consolelogjsonstringifydata



developersdevelopersplayerapisjavascriptapishostconfigurationmd
# hostconfiguration

hostconfiguration object allows retrieve information network interface internet connectivity

hostconfiguration


interface networkhost
hostconfig defaultconfig
promisehostconfig getconfig
promisevoid applyconfighostconfigwritable config


interface hostconfig
optional attribute string proxy
optional attribute arraystring proxybypasslist
optional attribute arraystring timeserverlist
optional attribute string timeserverinterval
optional attribute string hostname
optional attribute bool loginpassword
optional attribute bool forwardingenabled
optional attribute bool masqueradingenabled
optional attribute arraynatrule natlist


interface hostconfigwritable hostconfig
optional attribute stringor bool loginpassword
optional attribute stringor bool obfuscatedloginpassword


interface natrule
attribute natrulematch match
attribute natrulereplacement replace


interface natrulematch
attribute string protocol
optional attribute string sourceaddressrange
attribute string destinationaddressrange
attribute unsigned short destinationport


interface natrulereplacement
attribute string destinationaddress
attribute unsigned short destinationport



## Object Creation

create hostconfiguration object first load brightsignhostconfiguration module using require method create instance hostconfiguration class


hostconfigurationclass requirebrightsignhostconfiguration
hostconfigurationclass


## NetworkHost

interface retrieve modify host configuration

##### getConfig()


promisehostconfig getconfig


return hostconfig interface containing current hostconfiguration information

##### applyConfig()


promisevoid applyconfighostconfigwritable config


applies hostconfiguration setting player method accepts hostconfigwritable interface

config parameter contain complete desired configuration previous configuration overwritten wish change item keeping rest configuration call getconfig modify returned object example example section

## HostConfig

interface contains host configuration parameter

proxy string name address proxy server used http request proxy string formatted hostname contain four character character used replace octet current address example address currently 19216812 proxy proxy player attempt proxy named proxy192168

proxybypasslist arraystring list hostnames exempted proxy setting player attempt reach specified host directly rather using proxy specified proxy attribute example hostname examplecom would exempt examplecom examplecom proxy setting

timeserverlist arraystring array containing zero time server used player empty array disables automatic setting player clock single entry indicates time server protocol used supported protocol http http backwardcompatibility host name supported indicates used note using http host peer verification disabled since player clock correct following valid time server address





ntptimebrightsignnetworkcom

timebrightsignnetworkcom

timeserverinterval string value specifying often second player communicate time server adjust clock default interval hour minimum interval allowed second

hostname string player host name host name explicitly host name automatically generated based device serial number passing empty string method reset device host name automatically generated value

loginpassword bool value true mean password exists false mean password

forwardingenabled bool flag enables disables forwarding forwarding disabled false default

masqueradingenabled bool flag enables disables source address translation forwarding forwardingenabled true masqueradingenabled must specified true false

masqueradingenabled false datagrams forwarded interface address translation done

masqueradingenabled true datagrams forwarded interface snat applied datagrams sent upstream interface interface interface default route datagrams destined interface default route forwarded without

natlist arraynatrule list dnat rule let user change destination address port packet


## HostConfigWritable

interface contains password setting writing setting using applyconfig method member hostconfig interface special behavior

loginpassword string bool

string supplied set plaintext login password connection note must also enabled separately registry useful

boolean true supplied existing password left unchanged

boolean false supplied existing password removed

obfuscatedloginpassword string bool

except password previously obfuscated using shared secret contact supportbrightsignbizmailtosupportbrightsignbiz

learn generating obfuscation storing player


behavior ensures code getconfigthenc applyconfigc preserve existing password even though password returned getconfig

## NatRuleMatch

rule interface compared destination packet enter player packet field match property established natrulematch destination port overwritten desired value natrulesreplacement interface

protocol string filter entry must lower case

sourceaddressrange string optional filter range source address cidr format traffic source address included optional attribute specified

destinationaddressrange string range destination address cidr format overwritten

destinationport unsigned short destination port overwritten


## NatRuleReplacement

address port property specified natrulereplacement written packet replace selected address port property

destinationaddress string address replace previous address destination

destinationport unsigned short port replace previous port destination


## Examples

following script us applyconfig method hostname time server timeserver refresh interval


hostconfigurationclass requirebrightsignhostconfiguration
hostconfigurationclass

configdata
configdatahostname myplayer
configdataproxy
configdataproxybypasslist
configdatatimeserverinterval 1200
configdatatimeserverlist timebrightsignnetworkcom

consolelogconfiguring host
hcapplyconfigconfigdatathen
function
consolelogsuccess

catch
functiondata
consolelogjsonstringifydata



change item keeping rest configuration call getconfig modify returned object


hostconfiguration requirebrightsignhostconfiguration
hostconfiguration hostconfiguration
hostconfigurationgetconfig
thenfunctionconfig
confighostname hostbrightsign
hostconfigurationapplyconfigconfig

thenfunction
consolelogsuccess

catchfunctionerror
consolelogjsonstringifyerror



developersdevelopersplayerapisjavascriptapishtmlwidgetmd
# htmlwidget

htmlwidget object allows instantiate additional html browser

htmlwidget



constructorhtmlwidgetparams params
interface htmlwidget
void postmessageobject data
void close


interface htmlwidgetparams
attribute htmlwidgetrect rect
attribute string
optional attribute nodeparams node
optional attribute javascriptinjection javascriptinjection
optional attribute bool bsobjects
optional attribute storage storage
optional attribute string inspectorserver
optional attribute bool inputenabled
optional attribute security security
optional attribute string transform
optional attribute string hwzdefault
optional attribute bool interceptreloads


interface htmlwidgetrect
attribute long
attribute long
attribute long width
attribute long height


interface nodeparams
attribute bool enabled
optional attribute arraystring argument


interface javascriptinjection
optional attribute javascriptinjectiondetaillist documentcreation
optional attribute javascriptinjectiondetaillist documentready
optional attribute javascriptinjectiondetaillist deferred


interface javascriptinjectiondetail
optional attribute string world
optional attribute string source
optional attribute string
optional attribute string code


interface storage
attribute string path
attribute long quota
attribute bool forcesharedstorage
attribute bool forceunsharedstorage


interface security
optional attribute bool insecureoriginenabled
optional attribute bool cameraenabled
optional attribute bool desktopcaptureenabled
optional attribute bool audiocaptureenabled
optional attribute bool insecurehttpsenabled



## Object Creation

create htmlwidget object first load brightsignhtmlwidget module using require method create instance htmlwidget class


htmlwidgetclass requirebrightsignhtmlwidget
htmlwidget htmlwidgetclass rectx


## HtmlWidget

##### postMessage()


void postmessageobject data


sends asynchronous message child browser process child process brightsignmessageport object open message generate bsmessage event object payload javascript object must level deep cannot include nested object

##### close()


void close


shuts child browser process equivalent calling windowclose inside child browser nodejs parent process wont exit automatically html widget cant garbage collected widget closed

## HtmlWidgetParams

interface contains html widget parameter

rect htmlwidgetrect contains parameter size positioning widget

string display

node nodeparams optional contains parameter used specify added nodejs functionality

javascriptinjection javascriptinjection optional contains parameter specify javascript code inject different initialization point

bsobjects bool optional enables disables brightscriptjavascript object value disabled default

storage storage optional used configure html storage

inspectorserver string optional enables chromium inspector allows debug javascript application webpage running starting 8531 need also enablewebinspector registry html section enable javascript console

access console navigate player address specified port number page documentation relating javascript console

enablewebinspector allow inspector present disable reboot needed change take effect enabledisable ldws trigger reboot apply change


caution
security reason enablewebinspector used nonproduction presentation make sure disable javascript console publishing production environment chromium version found 8531 beyond javascript console information memory even connected inspector consume memory player run result crash

inputenabled bool optional enables mousetouchscreen event value false default

security security optional override chromium security check

transform string optional set screen orientation content widget note coordinate dimension rorectangle containing widget affected rotation following value accepted

identity transform widget content oriented landscape default setting

rot90 widget content rotated portrait degree clockwise

rot180 widget content rotated portrait degree clockwise

rot270 widget content rotated portrait degree clockwise

hwzdefault string optional specifies default behavior value default enable

interceptreloads bool optional prevents windowlocationreload similar construct taking effect browser instead parent receive reloadrequested event


## HtmlWidgetRect

interface allows size positioning widget rectangle

long specifies coordinate widget

long specifies coordinate widget

width long set width widget pixel

height long set height widget pixel


## NodeParams

interface allows enable nodejs define parameter nodejs commandline argument

enabled bool enables nodejsdevelopershtmldevelopmentnodejsmd widget value false default

argument arraystring optional array specifying commandline argument


##   
javascriptinjection

interface inject user script javascript engine

documentcreation javascriptinjectiondetaillist optional script soon document created behavior suitable operation

documentready javascriptinjectiondetaillist optional script soon ready behavior equivalent domcontentloaded event firing javascript

deferred javascriptinjectiondetaillist optional script page load finish


## JavascriptInjectionDetail

interface defines user script used javascriptinjection interface exactly source code field must defined

world string optional isolates user script different world string assigned following value application user main page detail world parameter included array application selected default

source string optional deprecated code instead

string optional defined must contain either file data following supported format

datatextjavascriptcharsetutf8

datatextjavascriptcharsetutf8base64

datatextjavascriptcharsetusascii

datatextjavascriptcharsetusasciibase64

code string optional defined content executed javascript code


## Storage

interface allows define following html storage parameter

path string folder used local storage application javascript storage class

quota long size byte allotted local storage application including indexeddb storage path specified without storage quota chromium default reserving plus total size storage device

forcesharedstorage bool allows httphttps loaded url share local storage loaded domain

forceunsharedstorage bool prevents file loaded url sharing storage


note
data corrupted html widget access database time application rely type access forceunsharedstorage flag avoid sharing local url experience data problem forcesharedstorage flag allow sharing httphttps site
flag file storage separated http storage

## Security 

override chromium security check parameter

insecureoriginenabled bool optional ignore insecure origin treat enabled

cameraenabled bool optional enables webpage access camera connected player access disabled default allows support webrtc application

desktopcaptureenabled bool optional enables desktop capture

audiocaptureenabled bool optional enables audio capture

insecurehttpsenabled bool optional ignore security error connecting insecure http host insecure http disabled default enabling feature make player insecure suitable production environment used testing


later chromium69 later several cors check added securityparamswebsecurity enablesecurityfalse disable check following registry setting instead

registry write html disablewebsecurity

flag take effect htmlwidget instance opposed previous flag effective instance called

write registry using roregistrysectiondevelopersbrightscriptobjectreferencehashingandstorageobjectsroregistrysectionmd


reghtml createobjectroregistrysection html
reghtmlwritedisablewebsecurity
reghtmlflush


developersdevelopersplayerapisjavascriptapisjavascripteventhandlingmd
# JavaScript Event Handling

## AddEventListener

addeventlistener common brightsign method used listen event

#### Syntax:


targetaddeventlistenertype listener


type string specifies type event listen

listener function object notified event specified type happens


## RemoveEventListener

removeeventlisteneris common brightsign method used remove event listener

#### Syntax:


targetremoveeventlistenertype listener


type string specifies type event listen

listener function object notified event specified type happens


## Example


function gpiocontroldownmsg

consolelogjsonstringifymsg
consolelog gpio msgdetail


event listener controldown gpio event

controlportaddeventlistenercontroldown gpiocontroldown

remove controldown gpio event listener

controlportremoveeventlistenercontroldown gpiocontroldown


developersdevelopersplayerapisjavascriptapiskeyboardmd
# keyboard

keyboard object allows configure input keyboard connected player

keyboard


interface keyboard
promisebool isattached
promisevoid setlayoutstring layoutname
promisevoid setnumlockbool onoff



## Object Creation

create keyboard object first load brightsignkeyboard module using require method create instance keyboard class


keyboardclass requirebrightsignkeyboard
keyboard keyboardclass


## Keyboard

interface allows detection configuration keyboard

##### isAttached()


promisebool isattached


return true keyboard connected player method count connected device keyboard report following key enter

##### setLayout()


promisevoid setlayoutstring layoutname


specifies localized layout attached keyboard setting take effect immediately persists registry reboot tabledevelopersbrightscriptobjectreferenceinputoutputobjectsrokeyboardmd valid keymap parameter player default

##### setNumLock()


promisevoid setnumlockbool onoff


set numlock state attached keyboard passed true reset state passed false

## Example


keyboardclass requirebrightsignkeyboard
keyboard keyboardclass
keyboardisattachedthen
functiondata
consolelogis attached
consolelogjsonstringifydata

catch
functiondata
consolelogjsonstringifydata

keyboardsetlayoutgbthen
functiondata
consoleloglayout

catch
functiondata
consolelogjsonstringifydata



developersdevelopersplayerapisjavascriptapiskeystoremd
# keystore

keystore object allows register client certificate player

package added using addcapackage method persistent individual certificate added using addcacertificate addclientcertificate method individual certificate must registered certificate database reboot

keystore


interface keystore
promisevoid addcacertificatestring filename
promisevoid addcapackagestring filename
promisevoid removecapackagestring filename
promisepackagelist getcapackagesinstalled
promisevoid addclientcertificateclientcertificateobject object


interface clientcertificateobject
attribute string certificatefile
attribute string passphrase
attribute string obfuscatedpassphrase




## Object Creation

create keystore object first load brightsignkeystore module using require method create instance keystore class


keystoreclass requirebrightsignkeystore
keystore keystoreclass


## KeyStore

interface certificate certificate database

##### addCaCertificate()


promise addcacertificatedomstring filename


register specified certificate certificate database client certificate either selfsigned signed using 3rdparty certificate issuer versign digicert

warning
chromium version later refuse sha1 certificate page information

##### addCaPackage()


promise addcapackagedomstring filename


add specified package file certificate database package name resides file need filename rokeystoredevelopersbrightscriptobjectreferencenetworkingobjectsrokeystoremd page information generating package

note
attempting modify package file added database invalidate package invalidated need removed database using removecapackage method added

##### removeCaPackage()


promise removecapackagedomstring filename


remove specified package certificate database getcapackagesinstalled method retrieve list package name database

##### getCaPackagesInstalled()


promisepackagelist getcapackagesinstalled


return list name package contained certificate database

##### addClientCertificate()


promise addclientcertificateclientcertificateobject object


register client certificate certificate database

## ClientCertificateObject

interface represents certificate file

certificatefile string file name path client certificate

passphrase string passphrase client certificate

obfuscatedpassphrase string obfuscated passphrase client certificate


caution
important
obfuscatedpassphrase passphrase required obfuscatedpassphrase take priority present recommend using obfuscatedpassphrase production environment passphrase used testing purpose contact supportbrightsignbizmailtosupportbrightsignbiz learn generating obfuscation storing player

## Example


requirebrightsignkeystore

kaddcapackagestoragesdexamplebscathen consolelogok consolelogfailed
kgetcapackagesinstalledthenpkgs consolelogpkgs
kremovecapackageexamplethen consolelogok consolelogfailed


developersdevelopersplayerapisjavascriptapismd
# JavaScript APIs



table content

javascript apis replace previous brightscriptjavascript objectsjavascriptapisreplacepreviousbrightscriptjavascriptobjects
enabling javascript apienablingthejavascriptapi
loading brightsign modulesloadingbrightsignmodules
synchronous asynchronous methodssynchronousandasynchronousmethods

brightsign javascript allows interface brightsign player firmware configure player retrieve system data interface peripheral device allows operation digital signage platformincluding playback scheduling diagnostics network configurationusing htmljavascript without need extensive coding brightscript

## JavaScript APIs Replace Previous “BrightScript-JavaScript Objects”

replaces brightscriptjavascript objectsplayerapisbrightscriptjavascriptobjectsmd older javascript object still offered backwardscompatibility purpose brightscriptjavascript migration guideplayerapisbrightscriptjavascriptmigrationguidemd mapping brightscript javascript apis

javascript object embedded browser runtime exist global javascript namespace used rohtmlwidget

thus javascript us node module work seamlessly rohtmlwidgetdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsrohtmlwidgetmd ronodejsdevelopersbrightscriptobjectreferencepresentationandwidgetobjectsronodejsmd roelectron superset legacy javascript object

brightsign added feature legacy brightscriptjavascript object several year current development effort javascript apis legacy brightscriptjavascript object exist support customer deployed software maintain support upgrade

unlike legacy brightscriptjavascript object onetoone relationship brightscript object object javascript many brightscript function http server file storage capability exposed javascript nodejs expose standardized popular equivalent

## Enabling the JavaScript API

brightsign javascript implemented nodejs module included chromium engine player brightsign rohtmlwidget instance must enable nodejs creating widget

##### **Example**


rcreateobjectrorectangle0019201080
aacreateobjectroassociativearray

aaurl
aanodejsenabledtrue

bbcreateobjectroassociativearray
bbport3000
aainspectorserverbb

hcreateobjectrohtmlwidgetraa
hshow


example nodejs enabled including nodejsenabledtrue entry associative array passed creation rohtmlwidget instance

## Loading BrightSign Modules

brightsign exist global window namespace javascript runtime instead like nodejs object brightsign module loaded using require function requirebrightsignmodulename brightsign module actually part firmware term usage identical nodejs module

##### **Example**


networkconfigclass requirebrightsignnetworkconfiguration call class constructor networkconfiguration object
wifi networkconfigclassethernet create instance networkconfiguration class


## Synchronous and Asynchronous Methods

brightsign module contain synchronous asynchronous method synchronous method return object used immediately asynchronous method return promise object return object data operation resolved script must handle delayed return typically using catch method available promise object

##### **Example**


networkconfigclass requirebrightsignnetworkconfiguration
wifi networkconfigclasswlan0
wifiscanthen call scan method return promise
functiondataconsolelogjsonstringifydata resolvesuccess case print scan result
catch
functiondataconsolelogjsonstringifydata rejectfailure case print failure reason


developersdevelopersplayerapismd
# Player APIs



developersdevelopersmd
# Developers

brightsign developer resource include documentation section well

## GitHub

brightsign github repository contains additional resource developer including plugins custom script

## BrightScript

brightscript language extension visual studio code facilitates brightscript coding used thousand developer around world

## MRSS Feed Generator

mrs feed generator batch file window generate mrs manifest file audiovideoimage file note

mrs feed file written folder

must edit batch file text editor configuration parameter

configuration parameter file interactive automated mode interactively provide diagnosticusage information


## Media List Feed Generator

medium list feed generator batch file window generate medium list feed specially formatted feed used feed source state

audio list

image list

video list

medium list

audio play file brightauthor

image play file brightauthor

video play file brightauthor

demand brightauthorconnected


note

contain audiovideoimage file folder

must edit batch file text editor configuration parameter

configuration parameter file interactive automated mode interactively provide diagnosticusage information

partnerspartnersbrightsignpartnerpacketautorunfilesmd
# Autorun Files

covered player provisioning consists applying setup player includes installation player player must contain autorunbrs file example instruct player display specific html file either local player external website alternatively autorun instruct player check particular updated presentation andor content file available download play

three autorunrelated file

autorunbrs also referred autorun autorun file

autorunzip

autozipbrs


similarsounding name term different function important conflate term

upon bootup player search certain file player search follows prescribed sequence shown

attachmentsimage20230413155338png

player search storage device predefined order

player first look autorunbrs file root directory first storage device encounter

found autorunbrs executed

autorunbrs file found player look autorunzip file root directory

autorunzip file found also contains within autozipbrs file player unzip autorunzip file process overwriting existing file storage device

player reboot

file found first storage device player repeat step next storage device available


autorunzip found storage device player query bsncloud provisioning service player previously provisioned bsncloud

autorunbrs autozipbrs must written brightscript given specific filename indicated

additional information file found

sample autorunbrs autozipbrs file reference

## Sample autorun.brs



autorunbrs file instructs player display local html file specifically indexhtml


main
create brightsign event handler
msgport createobjectromessageport

define screen viewing area
createobjectrorectangle 1920 1080

presentation resides either local external
config
fileindexhtml


create html event since presentation html file
createobjectrohtmlwidget config
hsetportmsgport
sleep10000
hshow

event loop ensure script run indefinitely
true
wait0 msgport
print typemsgtypemsg
typemsg rohtmlwidgetevent
eventdata msggetdata
typeeventdata roassociativearray typeeventdatareason rostring
print reason eventdatareason
eventdatareason loaderror
print message eventdatamessage
endif
endif
endif





## Sample autozip.brs



autozipbrs file instructs player unzip autorunzip file


name file autorunzip
content update application

main
path finddestpath
source findsourcepath
package createobjectrobrightpackage sourceautorunzip
packagesetpasswordtest
packageunpackpath
package
createdirectorypathbrightsigndumps
createdirectorypathpool
createdirectorypathfeedcache
createdirectorypathfeedpool

deletefilepathautozipbrs
deletefilesourceautorunzip
arebootsystem


function finddestpath
isfirmwarevalid
return


destinationpaths usb1
destination destinationpaths
ismounteddestination
return destination

next
return unknown
function

function findsourcepath
isfirmwarevalid
return


sourcepaths usb1
source sourcepaths
ismountedsource checkfilesourceautorunzip
return source

next
return unknown
function

function ismountedpath string
createobjectrostoragehotpluggetstoragestatuspathmounted
return true


return false
function

function isfirmwarevalid
createobjectrodeviceinfo
return difirmwareisatleast7060
function

function checkfilepath string
file createobjectroreadfile path
typefile roreadfile
return true


return false
function


next content source brightsignpartnerpacketcontentsourcesmd

partnerspartnersbrightsignpartnerpacketbrightsignpartnerresponsibilitiesmd
# BrightSign / Partner Responsibilities

highlevel responsibility expected brightsign partner follows

## BrightSign Expectations

brightsignos continuous development although provide advance notice roadmap guidance updated minimal notice responsibility individual partner manage player upgrade ensure stability environment

brightsign share code example provide guidance partner brightsign write partneroriented production code

brightsign provide quality assurance partner product


## Partner Expectations

partner responsible writing software integrates system brightsign player

partner responsible qualifying brightsignos update update player

partner public page listing supported brightsign player

refer earlier section document technical operational best practice optimize brightsign partner experience


next support brightsignpartnerpacketsupportmd

partnerspartnersbrightsignpartnerpacketbrightsignplayersmd
# BrightSign Players

brightsign player highly efficient embedded system specifically designed connectivity processing medium file player purposebuilt ground digital signage

## Software

brightsign operating system brightsignos opensource linuxbased based yocto openembedded project includes substantial brightsign modification include readonly root filesystem flash memory chromium rendering engine additional component audiovideo processing security

attachmentsimage20230626152212png

thanks builtin chromium engine brightsign player able htmljavascript application

brightsign player highly specialized although based linux generalpurpose linux cannot linux apps capable running apps android window however native android window able help leverage existing code natively player

attachmentsimage20230224203455png

brightsigns software component open source open source code freely available brightsigns website brightsign open source resource information

info
note term firmware occasionally used brightsigns documentation firmware refers brightsignos

## Hardware

brightsign player compact highlyefficient theyre fanless virtually silent performance maximized running video decoding encoding dedicated hardware

efficient heatdissipating enclosure moving part break brightsign player extremely reliable even theyre running hour day week indeed reliability longevity brightsign player widely viewed unmatched industry

learn current brightsign hardware lineup

next player setup provisioning brightsignpartnerpacketplayersetupprovisioningmd

partnerspartnersbrightsignpartnerpacketcontentsourcesmd
# Content Sources

thanks builtin chromium engine brightsign player generally display html page capable displayed chrome browser typically html presentation consist html file resides locally player storage device content displayed html file broadly categorized follows

local

content resides player storage device

since content local begin playing immediately



content retrieved external

unless content previously cached must first downloaded displayed

streamed

content streamed either locally external server

streamed content relies dedicated streaming server various streaming protocol like udprtprtsp http

video audio data transported continuous flow watched listened almost immediately without wait full download complete


category mutually exclusive player readily play content mixture content source

next example manual setup

partnerspartnersbrightsignpartnerpacketexamplemanualsetupattachmentsautorunautorunbrs
main

msgport createobjectromessageport
createobjectrorectangle 1920 1080

config
fileindexhtml


createobjectrohtmlwidget config
hsetportmsgport
sleep10000
hshow

true
wait0 msgport
print typemsgtypemsg
typemsg rohtmlwidgetevent
eventdata msggetdata
typeeventdata roassociativearray typeeventdatareason rostring
print reason eventdatareason
eventdatareason loaderror
print message eventdatamessage
endif
endif
endif




partnerspartnersbrightsignpartnerpacketexamplemanualsetupattachmentsautorunautozipbrs
name file autorunzip
content update application

main
path finddestpath
source findsourcepath
package createobjectrobrightpackage sourceautorunzip
packagesetpasswordtest
packageunpackpath
package
createdirectorypathfeedcache
createdirectorypathfeedpool
createdirectorypathbrightsigndumps

deletefilepathautozipbrs
deletefilesourceautorunzip
arebootsystem


function finddestpath
isfirmwarevalid
return


destinationpaths usb1
destination destinationpaths
ismounteddestination
return destination

next
return unknown
function

function findsourcepath
isfirmwarevalid
return


sourcepaths usb1
source sourcepaths
ismountedsource checkfilesourceautorunzip
return source

next
return unknown
function

function ismountedpath string
createobjectrostoragehotpluggetstoragestatuspathmounted
return true


return false
function

function isfirmwarevalid
createobjectrodeviceinfo
return difirmwareisatleast7060
function

function checkfilepath string
file createobjectroreadfile path
typefile roreadfile
return true


return false
function

partnerspartnersbrightsignpartnerpacketexamplemanualsetupattachmentsautorunindexhtml
doctype html
html
head
style
body backgroundcolor black
color white fontfamily sansserif


boxsizing borderbox


rowafter
content
clear
display table



float left
width
padding


videocontainer
position relative
paddingbottom 5625
paddingtop
height
overflow hidden


videocontainer iframe
videocontainer object
videocontainer embed
position absolute

left
width
height


slideshowcontainer
maxwidth
position relative
marginleftauto
marginrightauto
margintopauto
marginbottomauto
overflowhidden


myslides
displaynone


myslides
width100
heightauto


youtubecontainer
positionrelative
paddingbottom5625
height0
overflowhidden


youtubecontainer iframe
positionabsolute
top0left0width100height100


weathercontainer
positionrelative
paddingbottom5625

height auto
overflow hidden


style
head
body

classrow
classcol
h3video file localon playerh3
classvideocontainer
video width100 autoplay loop muted
source srcsnowyrivermp4 typevideomp4
video



classcol
h3streaming video youtubeh3
classyoutubecontainer
iframe width560 height315 frameborder0 allowfullscreeniframe




classrow
classcol
h3photos remote serverh3
classslideshowcontainer

classmyslides fade
stylewidth100


classmyslides fade
stylewidth100


classmyslides fade
stylewidth100





script
slideindex
showslides

function showslides

slide documentgetelementsbyclassnamemyslides
slideslength
slidesistyledisplay none

slideindex
slideindex slideslength slideindex
slidesslideindex1styledisplay block
settimeoutshowslides 5000 change image every second

script




classcol
h3weather widget urlh3
classweathercontainer
idww9b69f46d0b38e locauto atresponsivelangensllpl1idsfontarialslicsoneaslsotfahrenheitclbkgrgba0001clfontffffffclcloudffffffclpersp81d4faclsunffc107clmoonffc107clthundff5722cloddffffff17a href idww9b69f46d0b38eu targetblankfree weather androidadivscript async





body
html

partnerspartnersbrightsignpartnerpacketexamplemanualsetupconsiderationsmd
# Considerations

brightsign player highly versatile content source able utilize important factor considered making decision content source

displaying streaming content hosted external website requires persistent internet connection performance subject whim network connectivity internet issue player able reliably display content

common case digital signage player loop content repeatedly retrieve content server particularly multiple player player requires individual stream highly inefficient potentially expensive bandwidth server resource

content resides locally player much preferred quality service much tightly controlled dependent persistent network connection brightsign offer tool enable remote content delivery directly player well solution caching external content refer resource section guide player

brightsign player also capability directly running nodejs application streaming content desired player ability streaming server

case preferred content source local content cached content mixture

next integrating brightsign brightsignpartnerpacketintegratingwithbrightsignmd

partnerspartnersbrightsignpartnerpacketexamplemanualsetupcopytoplayermd
# Copy to Player

example maintain player default setup brightsign default setup manually copy autorunzip file player storage device autorunzip file install player

## autorun.zip

minimum autorunzip file include following file

autorunbrs

autozipbrs


required autorunzip file also include presentationcontent html file associated medium file player display autorunbrs file invokes everything player need contained single package delivery utilize approach example html file sample presentation

attachmentsimage20230327234103png

autorunzip file include following file

autorunbrs script shown previous section recall file instructs player render indexhtml

autozipbrs script shown previous section instructs player unzip autorunzip file

indexhtml html presentation

snowyrivermp4 sample video displayed indexhtml presentation


create version file compress autorunzip file autorunzip file attached

autorunzipattachmentsautorunzip

## Local + Remote Content

although including video file autorunzip file presentation also display following

streaming video youtube

picture slideshow picture retrieved external server

local weather displayed weather widget retrieves data external


brightsign player capable displaying combination local remote content

## Copy to Card

next manually copy autorunzip empty microsd card insert card player

attachmentsimage20230623164334png

copy autorunzip file root directory blank properly formatted microsd card

insert microsd card player

power player


shortly player boot something like display

attachmentsimage20230328161412png

## Folders

attachmentsimage20230526015203png

autorunzip file unpacked autozipbrs file instructs player create several folder root directory microsd card folder function follows

### brightsign-dumps

player crash dump created stored folder dump numbered incrementally useful troubleshooting requested brightsign support diagnosing problem note recent crash dump retained

### pool

medium file especially video file quite large help player better manage large file player apply cryptographic hash function medium file hash function well beyond scope document highlevel hash algorithm applied file unique hash alphanumerical representation file generated file changed file result completely different hash

hash typically many time smaller size compared original file whereas large video file easily gigabyte hash video dozen byte exact size hash depends algorithm used

hash therefore much manageable representation actual medium file pool formally asset pool hash stored system efficiency greatly improved hash system example quickly determine file changed simply based whether hash changed instead compare large file detail asset pool found

### feedPool

feedpool contains transient nonstatic asset like feed dynamic playlist used brightsign presentation

### feed\_cache

feedcache store metadata transient asset feedpool example feedcache would store feed identifier particular item feed item read one

next consideration examplemanualsetupconsiderationsmd

partnerspartnersbrightsignpartnerpacketexamplemanualsetuppreparationsmd
# Preparations

first need gather necessary material order follow along example

## What You Will Need

brightsign player associated power supply

microsd storage device microsd card assumed guide

microsd card adapter computer standard card reader typically require adapter access microsd card



display

hdmi cable connects player display


## Storage Preparation

make sure card properly formatted described

## Player Preparation

player brand player ready proceed

warning
previously player residual setting need reset particular player previously configured bsncontent perhaps evaluate service using free trial player attempt connect bsncontent refer instruction delete player provisioning record return proceed

next copy player examplemanualsetupcopytoplayermd

partnerspartnersbrightsignpartnerpacketexamplemanualsetupmd
# Example (Manual Setup)

section guided handson example demonstrates player manually provisioned simultaneously display local streaming content

many partner likely prefer remote provisioning manual provisioning example nevertheless useful introduces important info providing fundamental demonstration player function example straightforward replicate enables user easily follow along player remote provisioning covered later packet

covered previously provisioning player involves applying setup player player player setup explicitly applied brightsign default setup configures player look network connection ethernet connection found obtain address using dhcp example maintain brightsign default setup copy custom player player

next preparation examplemanualsetuppreparationsmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignappurlmd
# App URL

handson example player manually provisioned physically copying player player storage device since brightsign default setup acceptable provisioning player require setup explicitly applied

manual provisioning straightforward process pose challenge multiple player involved player remote hardtoaccess location andor content need updated frequently remote provisioning therefore highly beneficial many scenario

recommended method partner provisioning player either manually remotely setup freely created bsncontrol controlbsncloud

## App URL

publishing mode important setting included setup publishing mode effective remotely content onto player detail setup found summary follows

desired autorunbrs autorunzip file uploaded playeraccessible autorunzip file includes essential autozipbrs autorunbrs desired presentation file associated content file path autorunbrs autorunzip file designated example available

player configured several way

applied directly player group player provision screen accessible admin menu bsncontrol interface shown next section

create setup using bsncontrol interface info creating setup found

setup contains info

setup remotely applied player group internetconnected player

player download autorunbrs autorunzip file specified setup

player configured upon booting download autorunbr autorunzip file specified file autorunzip file containing autozipbrs file player unzip file player reboot autorunbrs file


image20240801165702pngattachmentsimage20240801165702png

next walk another handson example provision player directly

next example integratingwithbrightsignexampleappurlmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignbsncontrolintegrationmd
# bsn.Control Integration

partner highly encouraged take advantage free powerful tool offered bsncontrol common way partner utilize bsncontrol

swivel approach

integration partner bsncontrol


## “Swivel” Approach

easiest way partner running swivel chair approach method user utilize bsncontrol alongside partner

image20240801164748pngattachmentsimage20240801164748png

approach user full access capability bsncontrol unbranded interface controlbsncloud browser another browser bsncontrol user quickly swivel back forth bsncontrol

image2023021521371620240404194936pngattachmentsimage2023021521371620240404194936png

## API Integration

using brightsigns apis partner able design custom user interface access underlying function bsncontrol user interact single authoring publishing content management player management

image20240801165212pngattachmentsimage20240801165212png

next let take look way bsncontrol used remotely provision player

next integratingwithbrightsignappurlmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsigndevelopersetupmd
# Developer Setup

developer brightsign ecosystem several item help running efficiently possible mandatory item include everything listed earlier handson example listed convenience

brightsign player associated power supply

microsd storage device

using microsd card storage device also likely need microsd card adapter computer standard card reader typically require adapter access microsd card



display

hdmi cable connects player display


addition useful connect player local network ethernet cable player appropriate hardware wifi

## BrightSign Shell and BrightScript Debugger

partner also find brightsign shell brightscript debugger useful development purpose brightsign shell commandline interface enables interaction brightsignos operating system power brightsign player brightscript debugger enables interaction brightscript interpreter

brightsign shell page contains info various way access shell specific type cable prefer physical connection player command troubleshooting

brightsign debugger page contains info enable access debugger command troubleshooting

## Local DWS

diagnostic server powerful tool enables inspection various player setting diagnostic detail local diagnostic server ldws accessible local network player address remote diagnostic server rdws accessible either bsncontrol bsncontent bsncloud available general info found specific info rdws found

local apis also exist enable direct access functionality

## VSCode

visual studio code popular coding environment brightsign development brightscript language extension facilitates coding brightscript used thousand developer around world

next partner resource

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsigndevelopertoolsmd
# Developer Tools

brightsign offer extensive array developer tool listed alphabetical order

## BrightSign Shell & BrightScript Debugger

brightsign shell commandline interface enables interaction brightsignos serial cable telnetssh brightscript debugger tool facilitates debugging brightscript code info tool found

## Crash Dumps

player encounter nondeliberate shutdown crash crash dump generated upon reboot file contain useful information brightsign support analyze troubleshooting file found brightsigndumps folder located root folder player storage device

## Diagnostic Web Server

diagnostic server powerful tool enables inspection various player setting diagnostic detail local diagnostic server ldws accessible local network player address typing browser nnnnnnnnnn serial number remote diagnostic server rdws accessible either bsncontrol bsncontent bsncloud available general info found specific info rdws found

### Media Analyzer

includes useful tool analyze medium file playability info found

## HTML

html common format displaying presentation brightsign player html best practice document likely useful developer specific subsection document worth noting individually listed

### Web Inspector

page debugged local network using inspector

### Chromium Version

chromium version brightsign player likely several version behind version user using browser find chromium version specific firmware version player

development testing useful correct version chromium information found

## Logs / Diagnostics

log contain important diagnostic information player system log sometimes referred player log player available gathered syslog server telnet serial cable info accessing log mean found

refer article obtaining player log interpreting player log log easily accessed rdws described

## Node

node prompt commandline interface allows interact nodejs used javascript code execute nodejs command information node prompt well node inspectordebugger found

## Registry

registry object allows read write player registry player persistent memory info registry found

## Serial Ports

brightsign player serial port diagnostic purpose well provide interactive capability info hardware detail player serial port found serial port access brightsign shell brightscript debugger found

## Telnet and SSH

telnet used communicate brightsign player info found

## VSCode Extension for BrightScript

popular brightscript language extension vscode facilitates writing brightscript used thousand developer around world note brightsigns brightscript fork rokus brightscript fork diverged similar technically value mainly brightscript syntax highlighting

next provide recommended developer setup help maximize efficiency developing brightsign platform

next developer setup integratingwithbrightsigndevelopersetupmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignexampleappurlmd
# Example (App URL)

example provisioning player publishing mode

## Player Preparation

better reflect likely experience realworld user proceed player brand

previously used player follow along manual setup example simply erasereformat storage device reinsert player since player explicitly provisioned bsncloud brightsign default setup used player need reprovisioned

previously activated player bsncloud however refer direction delete player provisioning record return

warning
example provisioning player prior booting player first time player already provisioning record bsncloud powering player take user activation screen activation provision player current default setup unless another default setup created player provisioned brightsign default setup us bsncontent publishing mode reprovisioning player would required apply different setup provisioning player prior activating player thus save step reprovision player

## Provision Player

power player

write player serial number serial number found label bottom player label player packaged

admin provision player enter serial number wrote desired also enter optional player name player description

select player


attachmentsimage20230914201123png

player appear list player note assigned default setup explicitly created default setup default setup brightsign default setup

next

select player wish provision player serial number added

select apply dropdown menu

popup window select enter desired autorunzip file resides like example

select apply


attachmentsimage20230914201639png

player provisioned publishing mode player setting since explicitly changed remain brightsign default setup

## Power Up Player

power player player booted search provisioning record bsncloud record found player apply setting according provisioning record since created provisioning record player previous step player apply setting case provisioning record instructs player designated download autorunzip file unzip file reboot autorunbrs within autorunzip file autorunbrs file configured display html presentation contained autorunzip file

presentation previously displayed manual copy example shown screen whereas previous example autorunzip file manually copied player storage device player remotely provisioned retrieve autorunzip file

next developer tool integratingwithbrightsigndevelopertoolsmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignonboardingmd
# Onboarding

every partner different need perspective meeting partner integration engineering team help path best suited need connect team integrationsbrightsignbizmailtointegrationsbrightsignbiz started creating integration plan

partner typically follow process integrate brightsign

sign ndas

brightsign share relevant documentation

documentation read technical call discus technical detail integration

partner develops integration brightsign player

technical issue arise development brightsign provide support ticketing system

partner test approves code

technical integration complete partner fill selfcertification form required comarketing activity brightsign

integration packaged handed gotomarket team


maximize chance successful integration recommend adhere guideline technical best practice

next technical best practice brightsignpartnerpackettechnicalbestpracticesmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignpartnerresourcesmd
# Partner Resources

## Caching

detail html caching found

## JavaScript

information javascript found

## Node.js

detail nodejs brightsign player found

## REST APIs

brightsign offer rest apis enable partner interface player detail

## Extensions

case desired functionality accomplished various tool resource available extension useful certain circumstance generally discouraged longterm support reason feel extension necessary application please inquire integrationsbrightsignbizmailtointegrationsbrightsignbiz assistance regarding specific situation

next cover partner onboarding process

next onboarding integratingwithbrightsignonboardingmd

partnerspartnersbrightsignpartnerpacketintegratingwithbrightsignmd
# Integrating with BrightSign

shown handson example brightsign player provisioned manually copying necessary file player storage device approach feasible small number easily accessible player requiring infrequent content update manual approach quickly becomes untenable larger network player difficult access andor situation regular content update desired

fully take advantage brightsign offering partner encouraged utilize many powerful tool brightsign offer help streamline deployment management player

next bsncontrol integration

partnerspartnersbrightsignpartnerpacketoperationalbestpracticesmd
# Operational Best Practices

based experience partner follow practice successful brightsign integration

encourage report issue help resolve contact integrationsbrightsignbizmailtointegrationsbrightsignbiz support

integration issue arise partner communicates support team partner customer

ensure ongoing alignment brightsigns technology partner goal encourage partner proactive talk making major change existing integration

partner aware brightsign fully test experimental feature component chromium experimental feature used part integration stability adversely affected


next cover responsibility expected brightsign partner

next brightsign partner responsibility

partnerspartnersbrightsignpartnerpacketpartnerglossarymd
# Partner Glossary



table content

autorunbrsautorunbrs
autorunzip autozipbrsautorunzipandautozipbrs

brightauthorconnectedpartnerglossarybrightauthorconnected
brightscript debug consolepartnerglossarybrightscriptdebugconsole
brightsign shell consolepartnerglossarybrightsignshellconsole
bsncloudpartnerglossarybsncloud
bsncontrolbsncontrol
bsncontentbsncontent
chromiumpartnerglossarychromium
consolepartnerglossaryconsole
cmspartnerglossarycms
content deliverypartnerglossarycontentdelivery
content presentationpartnerglossarycontentpresentation
crash dumpspartnerglossarycrashdumps
diagnostic serverpartnerglossarydiagnosticwebserver
medium analyzermediaanalyzer
htmlpartnerglossaryhtml
inspectorwebinspector
chromium versionchromiumversion
log diagnosticspartnerglossarylogsdiagnostics
nodepartnerglossarynode
partner apppartnerglossarypartnerapp
playerpartnerglossaryplayer
provisioningpartnerglossaryprovisioning
registrypartnerglossaryregistry
serial portspartnerglossaryserialports
setuppartnerglossarysetup
storage devicepartnerglossarystoragedevice
swivelpartnerglossaryswivel
telnet sshpartnerglossarytelnetandssh
visual studio codepartnerglossaryvisualstudiocode
code extension brightscriptpartnerglossaryvscodeextensionforbrightscript

## autorun.brs

upon bootup player look autorunbrs file instructs player upon startup file required player

## autorun.zip and autozip.brs

player also look autorunzip file contain script autozipbrs found player execute autozipbrs unpacks content autorunzip file root directory storage device reboots player

# BrightAuthor:connected

software available provides easytouse interface creating presentation create assign player schedule monitor player status health player software also enables user setup activate provision player well manage user role permission

# BrightScript Debug Console

brightscript debug console tool facilitates debugging brightscript code available brightsign shell turn brightscript debug console type script debug console info found

# BrightSign Shell / Console

brightsign shell also referred brightsign console command line interface enables interaction brightsign serial cable telnetssh

brightsign shell script command used access brightscript debug console node command used access node related function

command brightsign shell found

# BSN.cloud

brightsigns robust cloudbased platform provides myriad tool service help customer partner easily single player manage expansive network player bsncloud consists different option free bsncontrol paid bsncontent

## bsn.Control

free solution enables viewing player information player provisioning remote diagnostics access rest apis

## bsn.Content

paid solution includes feature bsncontrol plus content hosting ability create schedule publish content advanced network management tool user group role privilege

# Chromium

chromium free opensource browser project primarily developed maintained google underlying engine ubiquitous chrome browser brightsign player chromium software render display content

# Console

informal name brightsigns command line interface

# CMS

might surmised content management system used manage content cmss also often used manage player setup activation provisioning scheduling diagnostics

separate apps used author publish presentation guide term catchall term refer software enables authoring publishing management presentation content player

# Content Delivery

term used describe process getting content onto player storage device

# Content / Presentation

strictly speaking presentation refers file control layout behavior item player display

content refers visual item displayed presentation content thus refers medium file associated presentation video image audio file

since presentation content depend render properly cannot displayed without term content generally used represent presentation content

# Crash Dumps

player encounter nondeliberate shutdown crash crash dump generated upon reboot file contain useful information brightsign support analyze help troubleshoot file found brightsigndumps folder located root folder player storage device

detail crash report found

# Diagnostic Web Server

diagnostic server powerful tool enables inspection various player setting diagnostic detail local diagnostic server ldws accessible local network player address remote diagnostic server rdws accessible either control cloud content cloud bsncloud available general info found specific info rdws found

## Media Analyzer

includes useful tool analyze medium file playability info found

# HTML

html stand hypertext markup language standard markup language page creation also common format displaying presentation brightsign player html best practice document likely useful developer specific subsection document worth noting individually listed

## Web Inspector

page debugged local network using inspector

## Chromium Version

chromium version brightsign player likely several version behind version user using browser find chromium version specific firmware version player

development testing useful correct version chromium information found

# Logs / Diagnostics

log contain important diagnostic information player system log sometimes referred player log player available gathered syslog server telnet rs232 serial cable info found

refer article obtaining player log interpreting player log log easily accessed rdws described

# Node

node prompt commandline interface allows interact nodejs used javascript code execute nodejs command

# Partner App

partner application partner refers partner software resides player storage device case partner consists presentation partner wish player display upon bootup player run autorunbrs file configured invoke partner

# Player

brightsigns extensive line hardware device specifically designed digital signage

# Provisioning

term generally refers process activating player getting autorunbrs file onto player storage device

# Registry

registry object allows read write player registry player persistent memory info registry found

# Serial Ports

brightsign player serial port diagnostic purpose well provide interactive capability info serial port found

# Setup

setup file containing information intended publishing configuration various player setting setup applied many player different setup saved setup library

# Storage Device

brightsign player lack onboard storage require separate storage device storage device include microsd card well drive thumb drive external hard drive external solidstate drive ssds many brightsign player also support internal ssds common form factor

# Swivel

official term word swivel sometimes used describe partner integration user interact partner using browser interacting control cloud interface another browser

# Telnet and SSH

telnet network protocol allow connect remote computer internet telnet older protocol used remote access server networking device sends data plain text without encryption authentication make insecure secure shell newer protocol provides secure remote access server networking device encrypts data sent client server making much secure telnet also us public authentication added security

telnet used communicate brightsign player info found

# Visual Studio Code

visual studio code code sourcecode editor made microsoft electron framework window linux macos used editing text managing entire codebase like integrated development environment support debugging syntax highlighting intelligent code completion snippet code refactoring embedded

# VS Code Extension for BrightScript

popular brightscript language extension vscode facilitates coding brightscript used thousand developer around world note brightsigns brightscript fork rokus brightscript fork diverged similar technically nevertheless developer find value extension

partnerspartnersbrightsignpartnerpacketplayersetupprovisioningmd
# Player Setup / Provisioning

info
bsncontrol bsncontent formerly named control cloud content cloud respectively

## Player Setup

covered start section player must first much anything process involves applying setup player setup applies various setting player network setting publishing mode logging includes player provides instruction player upon startup

image20240404165839pngattachmentsimage20240404165839png

## Player Provisioning

also mentioned start section term provisioning refers using bsncloud player given bsncloud either bsncontrol bsncontent tier used vast majority time player term provision often used referring player setup

primary case player properly instead provisioned bsncloud used apply setup player

standalone player configuration setup manually copied storage device storage device connected player

uncommon situation partner chooses player without using bsncloud


bsncloud provisioning player nearly automatic thing properly beforehand player automatically provisioned plugging customer cant dont want connect player internet offline provisioning option also available

info
provisioning player done free using either brightauthorconnected unbranded bsncontrol interface controlbsncloud however since controlbsncloud interface preferred partner guide largely focus using controlbsncloud

## Setup

setup created using free unbranded bsncontrol interface controlbsncloud setup saved setup library used modified future

created setup applied player group player using controlbsncloud alternatively information contained setup directly incorporated player described manually copied player storage device

### Player Settings

setup establishes various player setting include thing like publishing mode network setting ethernet wifi player identification name description logging

### Player App

file folder instruct player upon boot collectively known player minimum player must contain autorunbrs file extension denotes brightscript file instructs player upon startup

setup applied player bsncloud autorunbrs file automatically created player

partner write custom player apps according specific need example player designed connect partner download content player display

info
term partner sometimes used referring partner player

info setup found info provisioning found

next player provisioning recovery system requirement playersetupprovisioningplayerprovisioningandrecoverysystemrequirementsmd

partnerspartnersbrightsignpartnerpacketsupportmd
# Support

dive detail integration technical question inevitably arise many question answered support site

assistance needed help created ticketing system help manage track issue ticketing system ensures efficient routing issue directly relevant team within brightsign make easier party involved stay updated issue status

issue question emailed integrationsbrightsignbiz trigger ticket created important thing keep mind

issue question team generated ticket create ticket email integrationsbrightsignbiz message coming email domain get automatically routed priority queue partner

please refer next section tip create good support ticketsupportwritingagoodsupportticketmd providing necessary detail ticket outset help ticket resolved efficiently possible

reply ticket simply reply email sent ticketing system

ticketing system also accessed generally speaking primary benefit view open item case easiest reply email ticketing system


always excited hear customer feature request feedback made brightsign product feature request discussion forum product management team us communityforum track request user youre make sure upvote feature think would useful future release

requesting technical support important include relevant information next provide guideline writing good support ticket

next writing good support ticket supportwritingagoodsupportticketmd

partnerspartnersbrightsignpartnerpackettechnicalbestpracticesmd
# Technical Best Practices

assist partner getting running efficiently possible weve compiled list technical best practice maximize chance success

## brightsign-dumps Folder

developing autoruns forget include instruction autorun create brightsigndumps folder player brightsigndumps folder used store crash information useful brightsign support troubleshooting

## Free Tools

brightsign offer plethora free tool service greatly ease provisioning diagnostics include powerful tool available bsncontrol player provisioning well many tool described developer toolsbrightsignpartnerpacketintegratingwithbrightsigndevelopertoolsmd section guide partner highly encouraged take much advantage tool possible accelerates development also make support troubleshooting much easier

## Memory Management

brightsign player purposebuilt digital signage player generalpurpose device require much memory typical developing brightsign platform developer cognizant potential memory limitation accustomed

## OS Updates

partner latest brightsignos build order take advantage latest fix newest feature keeping date latest build also enables partner easily expand deployment latest hardware

continuously improving firmware player often case software problem sometimes inadvertently introduced stable player paramount brightsign integration strongly encourage partner thoroughly test brightsign firmware release prior upgrading player used production environment

## HTML <video> Elements & Memory

fairly common presentation include switching video another many brightsign player including series line video element explicitly released element continue memory even longer actively displaying therefore important reset source blank prior switching video done first video continue memory subsequent video playing potentially resulting following message

failed find video decoder

release video element attribute video blank

videosrc

additional detail topic found

## Smooth Video Transitions

multiple video displayed sequentially generally desired video transition smoothly help ensure make sure first last frame video consist blank frame presence even blank frame video result noticeably jarring transition video

## Upgradeability

change inevitable partner recommended design apps ability push update player remotely applies partner also diagnostic script useful troubleshooting

next operational best practice brightsignpartnerpacketoperationalbestpracticesmd

partnerspartnersbrightsignpartnerpacketmd
# BrightSign Partner Packet

attachmentsbrightsign20partner20packet20230120182258png

welcome brightsign partner packet document serf introductory guide integration partner content management system brightsign ecosystem includes brightsigns extensive array digital signage player well rich player management service

partner able build application allow customer publish manage brightsign player brightsigns development technology including open apis enable seamless partner integration

offer service support multiple worldwide location partner integration business development marketing team dedicated helping partner every step initial inquiry onboarding market launch

warning
attention partner
brightsigns product service highly differentiated function unique way brightsign highly recommended start section provides quick highlevel overview product service work

partner already good understanding player service function let started

page next link bottom take next page packet alternatively skip pagesection packet using collapsible page tree left

next brightsign player brightsignpartnerpacketbrightsignplayersmd

partnerspartnersbsncloudforpartnersaddingpartnercmsplayerstoabsncloudnetworkmd
# Adding Partner CMS Players to a BSN.cloud Network

player configured partner application also bsncloud network connection access player configuration maintenance temporary replace partner autorun autorunbrs make change needed connect bsncloud process described

## Prerequisites

must able access player local browser

must know name target bsncloud network

need registration token appendix instruction

getting token must download cloudparametersjson file appendix customize

edit line registration token

edit line target network name save file


## Replace the Autorun and Reboot the Player

open local player adding bsncloud

upload cloudparametersjson file card

download open standaloneautorunbrs file appendix saved cloudparametersjson file different name card make sure line standaloneautorunbrs reference correct name

upload standaloneautorunbrs card

local locate autorunbrs file

select cog icon shown image rename section

rename autorunbrs autorunbackup

rename standaloneautorunbrs autorunbrs

control local reboot player

player appear brightauthorconnected network rebooted autorunbrs reference partner application


image20240305163734pngattachmentsimage20240305163734png

## Appendix

### BRS and JSON Files

cloudparametersjsonattachmentscloudparametersjson
standaloneautorunbrsattachmentsstandaloneautorunbrs

### Getting a Registration Token through BSN.cloud

create setup package bsncloud

select save setup choose location save package computer

open folder saved package open currentsyncjson file

file find similar script image long string bsnregistrationtoken registration token string account match target network name inserted step


screenshot 20240305 82820 ampngattachmentsscreenshot202024030520at208282020ampng

### Getting a Registration Token through an API

first oauth token correctly issued target network token entity

partnerspartnersbsncloudforpartnersapplyingsettingsinthepropertiespanelmd
# Applying Settings in the Properties Panel



table content

prerequisitesprerequisites
implementing setting handler disabling property lockimplementingthesettingshandlerdisablingpropertylock
specificationapispecification
post apiv1systemsupervisorcapabilitiespostapiv1systemsupervisorcapabilities
request bodyrequestbody
response bodyresponsebody
example scriptexamplescript
caveatscaveats

brightsigns version 8272 brightauthorconnected version 1629 contain feature let user modify setting using bsncloud property panel bsncloud avoid backwards compatibility issue supervisor wont honor setting unless first enabled custom presentation custom applicationplugin

feature natively supported enabled brightauthorconnected presentation using version 1629 later must enable running custom script step required enable feature described

## Prerequisites

must using bsncloud

minimum brightauthorconnected version 1629

minimum version 8272


## Implementing the Settings Handler / Disabling Property Lock

player control bsncloud default disallow update pushed cloud player using partner application allow player accept property update bsncloud implement setting handler allows disable property lock partner using example script page

enable setting handler

include code snippet example script section custom presentation custom applicationplugin

brightauthorconnected navigate player network network right section player setting available property panel


deviceside turned player setting accessible property panel brightauthorconnected network

## API Specification

specification used custom presentation plugins either invoked brightscript javascript enable setting panel setting handler

base player ipv4 address default port server hosted

note
internal endpoint respond node javascript application running player part local

### POST /api/v1/system/supervisor/capabilities

#### Request Body



script
type custom
version 10060 version format used communicate script version bsncloud
displayed setting panel



#### Response Body

success successtrue

error status error status code message error message


## Example Script

partner want upgrade feature must include following code snippet brightsign presentation plugin

note example simple autorun however enablesettingshandler subroutine either copied called appropriate location relative logic script code within enablesettingshandler copied pasted valid location script within existing logic assumes developer basic knowledge brightscript


main
enablesettingshandler


enablesettingshandler
localbaseurl
supervisorapiv1route apiv1

supervisorcapabilitiesurlxfer createobjectrourltransfer
supervisorcapabilitiesurlxfer localbaseurl supervisorapiv1route systemsupervisorcapabilities
supervisorcapabilitiesurlxferseturlsupervisorcapabilitiesurlxfer
supervisorcapabilitiesurlxfersettimeout15000
supervisorcapabilitiesurlxfersetproxybypass127001 localhost
supervisorcapabilitiesurlxferaddheadercontenttype applicationjson

msgport createobjectromessageport
supervisorcapabilitiesurlxfersetportmsgport
initiatoridentity supervisorcapabilitiesurlxfergetidentity

script createobjectroassociativearray
scripttype custom
version 10060 current autorun script version

scriptaddreplacetype scripttype
scriptaddreplaceversion version

body
bodyaddreplacescript script

stringifiedjson formatjsonbody

supervisorcapabilitiesurlxferasyncpostfromstringstringifiedjson


print failed send post request
else
print setting handler request sent


true
wait0 msgport
typemsg rourlevent
receivedidentity msggetsourceidentity
initiatoridentity receivedidentity
print supervisorcapabilitiesurlxfer response code strimsggetresponsecode







## Caveats

setting handler override custom setting applied setup script

edits property sheet setting interface applied device side unless code snippet added runtime application added plugin custom presentation

partnerspartnersbsncloudforpartnerscontrolbsncloudmd
# Control.BSN.cloud

control cloud solution allows partner automate player device provisioning also known bdeploy monitor network brightauthorconnected examine problem remote diagnostic server page basic feature manage brightsign player network control cloud accessed controlbsncloud

# Device Provisioning (B-Deploy)

device provisioning service allows automated provisioning brightsign player internet order device provisioning partner need provide maintain application accessible http file server host package contained autorunzip file containing presentation file along autozipbrs boilerplate script case script need modified

package hosted device setup made brightauthorconnected point player directly application open brightauthorconnected sign bsncloud select cloud network desired device setup option make externally hosted application custom application option requires link manually input field partner application option provides drop menu application officially registered device provisioning server application added drop contact partner integration team setup file library done

attachmentssetupfigurepng

navigate admin device provisioning page select device enter serial number player desired process register player currently selected bsncloud network check mark box player apply setup alternatively clicking download template download microsoft excel file contains column serial number device name setup file application description excel sheet used help expedite process adding multiple serial number simultaneously automatically assigning setup file application url

attachmentsprovisioningfigurepng

everything entered correctly player automatically query device provisioning server connected internet powered device provisioning server assign player corresponding setup file point application url entered player automatically configure play presentation file contained autorunzip information device provisioning please page

## Re-provisioning vs. Factory Resetting a Player

cloud connected player reprovisioned rather factory reset must refreshed

warning
note
player reprovisioned currently configured network requires specification configuration security certificate wifi player chose current device setting device setup network configuration bottom left maintain player current network configuration

factory reset used local access player since deletes registry section clear network interface factory reset leave remote player inaccessible state would possible factory reset player reconnect bsncloud user device provisioning entry brightauthorconnected network allows rogue device retrieve active address bdeploy connection

# Remote Diagnostic Web Server

control cloud also offer access remote diagnostic server administrator monitor health player network well view modify setting player internet access open brightauthorconnected either application webtop service controlbsncloud sign select network registered player network health status click gear icon right desired player enter

info provide basic info snapshot time player model number address ipv6 address version time

attachmentsinfofigurepng

provides remotely download player troubleshooting purpose

attachmentslogfigurepng

control allows admins reboot player without crash report factory reset player change recovery disable local access reprovision device remotely

attachmentscontrolfigurepng

allows remote uploading file directly card however file size cannot exceed 10mb

attachmentssdfigurepng

diagnostics contains various diagnostic tool

attachmentsdiagfigurepng

network configuration allows admins view network configuration selection player

network neighborhood allows admins view information network neighborhood player

network diagnostics run network diagnostics player

network packet capture allows admins network packet capture packet capture ethernet wifi modem file size exceeding 10mb cannot downloaded

lookup allows admins test name resolution hostname

disable autorun disables currently script reboots player

ping ping address

storage formatting format inserted player

trace route performs route tracing address hostname


snapshot pull realtime snapshot content displayed player

attachmentssnapshotfigurepng

video display current video mode allows manual adjustment required well toggle power save option

attachmentsvideofigurepng

advanced provides registry dump ability update player

attachmentsadvancedfigurepng

partnerspartnersbsncloudforpartnerspartnersetupandrecoverymd
# Partner Setup and Recovery

1652 higher version brightauthorconnected bsncloud autorun download partner setup local place card useful advanced network configuration require player able reach internet download partner application also recovery example card corrupted need either reformatting replacement player automatically configured recovery workflow unlike bdeploy workflow player download template upload provisioning filepartnersetupandrecoveryprovision workflow

warning
must disable autorun reformatting card device
disable autorun v1controlreboot body parameter autorundisable described page also done local diagnostics

save setup package card brightauthorconnected

choose partner application setup type select partner image

select save setup file package saved card

factory reset player

install card

reboot player


next recovery partner application

brightauthorconnected admin device provisioning device

device serial number check next player list

action dropdown choose apply application

choose partner application partner previously selected

select apply


attachmentsscreen20shot202022061420at203551220pmpng

partnerspartnersbsncloudforpartnersmd
# BSN.cloud for Partners

bsncloud nextgeneration cloudbased infrastructure networked brightsign player section includes documentation bsncloud service including following



cloud apis overview brightsign rest apis

partnerspartnerspowerbiannouncementmd
# Power BI Announcement

microsoft announced chromium minimum browser supported power change brightsign upgrade current chromium browser version series player accommodate power user

## Series 5

current 901451 release contains beta version chromium version exceeds power requirement series using chromium110 registry

next release available august upgrade beta chromium version version functionality registry considered beta eventually move release contain chromium default version offer significant performance improvement enhanced security access latest technology

page information changing registry setting brightauthorconnected

### Registry Key Example Settings

must reboot updating registry apply change

#### DWS  

dont forget authentication curl command


curl location request
header contenttype applicationjson
digest usernamepassword
dataraw value chromium110


#### BrightScript Console

page information


registry write html widgettype chromium110


#### BrightScript

page information


reghtml createobjectroregistrysection html
reghtmlwritewidgettype chromium110
reghtmlflush


#### JavaScript

page information


registryclass requirebrightsignregistry
registry registryclass
registrywritehtml widgettype chromium110
consolelogwrite successful
catcherror
consoleerrorwrite failed error



#### TypeScript

page information


import registryclass brightsignregistry
const registry registryclass
registrywritehtml widgettype chromium110
consolelogwrite successful
catcherror error
consoleerrorwrite failed error



#### Player CLI

brightsignbsc tool information


local registry player playername value chromium110 section html widgettype


## Series 4

brightsign plan release chromium beta august help customer using power investigating version unify series version

## Series 3

brightsign investigating series product line hardware capability order provide higher chromium version

warning
beta version contain functional difference production

partnerspartnersupdatingbosfromhtmljavascriptapplicationsmd
# Updating BOS from HTML/JavaScript Applications



table content

accessing bosaccessingthebos
installing updateinstallingtheupdate
code requirementscoderequirements
selecting download locationselectingadownloadlocation
exampleexample
checking boscheckingthebos

brightsign partner htmljavascript application brightauthorconnected interface follow step outlined update latest

## Accessing the BOS

downloads section website previousbosreleases download version want

click download button download page corresponds model number brightsign player note version different model family often designated number different file make sure update file corresponds model number brightsign player

unzip downloaded file

bsfw file known location


contact supportbrightsignbizmailtosupportbrightsignbiz need help creating correct release

## Installing the Update

install update code must download update root directory attached storage device look reboot reboot player download also want check downloaded correctly

### Code Requirements

specify correct version bsfw downloaded

know download update specify location code code must decide write update file selecting download location guidance

download downloadfile function nodefetch module preferred method

call reboot function download brightsignsystem

brightsigndeviceinfo make sure downloaded correctly device


### Selecting a Download Location

writable storage device sufficient space recommend implement search order prefers faster durable device prioritize plugged stick storage primary take precedence secondary card user plug take precedence example

storageusb1 drive storage device connected player

storagesd primary microsd drive player

storagesd2 internal microsd drive player 4kx42 xdx32 model

storagessd internal player xtx44 xtx43 xdx34 xdx33 model


script iterate mountpoints storage skipping anything thats mountpoint tmpfs readonly looking drive enough space

## Example

code illustration purpose production implementation also contain step handle error data overflow writeprotected storage device

want youll need nodejs enabled browser runtime also edit point correct

osyouwant correct version

fwname bsfw filename

public store brightsign bsfw file

devicepath write update storage device



fetch
requirefs
path requirepath
fetch requirenodefetch

const systemclass requirebrightsignsystem
system systemclass
const diclass requirebrightsigndeviceinfo
diclass

information hardcoded specify osyouwant fwname variable
osyouwant 8282
fwname malibu8282updatebsfw

devicepath storagesdfwname


const downloadfile async path
const await fetchurl
const filestream fscreatewritestreampath
await promiseresolve reject
resbodypipefilestream
resbodyonerror
rejecterr

filestreamonfinish function
resolvesuccess





function main
diosversioncompareosyouwant
downloadfileurl devicepaththen
consolelogosyouwant downloaded successfully
systemreboot

catcherr
consolelogerr


else
consolelogyou gotten right osyouwant want



main


## Checking the BOS

player reboots check brightsign version brightauthorconnected make sure updated correct version

partnerspartnersmd
# Partners

collapse

expand collapse
