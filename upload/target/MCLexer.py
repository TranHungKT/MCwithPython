# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u015a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2g\n\2\r")
        buf.write("\2\16\2h\3\2\3\2\3\3\3\3\3\3\3\3\7\3q\n\3\f\3\16\3t\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\177\n\4\f\4")
        buf.write("\16\4\u0082\13\4\3\4\3\4\3\5\6\5\u0087\n\5\r\5\16\5\u0088")
        buf.write("\3\6\3\6\5\6\u008d\n\6\3\6\6\6\u0090\n\6\r\6\16\6\u0091")
        buf.write("\3\7\3\7\5\7\u0096\n\7\3\7\3\7\3\7\5\7\u009b\n\7\3\7\3")
        buf.write("\7\3\7\5\7\u00a0\n\7\3\7\3\7\3\7\5\7\u00a5\n\7\5\7\u00a7")
        buf.write("\n\7\3\b\3\b\3\b\3\b\7\b\u00ad\n\b\f\b\16\b\u00b0\13\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\7/\u013f")
        buf.write("\n/\f/\16/\u0142\13/\3\60\3\60\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u014a\n\61\f\61\16\61\u014d\13\61\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u0153\n\62\f\62\16\62\u0156\13\62\3\62\3\62\3\62")
        buf.write("\3r\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63\3\2\f\5\2\13\f\17")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2\62;\4\2GGgg\n\2$$))^^ddhhpp")
        buf.write("ttvv\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\t\2$")
        buf.write("$^^ddhhppttvv\6\2\n\13\16\17$$^^\2\u016c\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\3f\3\2\2\2\5l\3\2\2\2\7z\3\2\2")
        buf.write("\2\t\u0086\3\2\2\2\13\u008a\3\2\2\2\r\u00a6\3\2\2\2\17")
        buf.write("\u00a8\3\2\2\2\21\u00b4\3\2\2\2\23\u00b6\3\2\2\2\25\u00b8")
        buf.write("\3\2\2\2\27\u00ba\3\2\2\2\31\u00bc\3\2\2\2\33\u00bf\3")
        buf.write("\2\2\2\35\u00c2\3\2\2\2\37\u00c4\3\2\2\2!\u00c7\3\2\2")
        buf.write("\2#\u00c9\3\2\2\2%\u00cb\3\2\2\2\'\u00cd\3\2\2\2)\u00d0")
        buf.write("\3\2\2\2+\u00d3\3\2\2\2-\u00d5\3\2\2\2/\u00d8\3\2\2\2")
        buf.write("\61\u00e0\3\2\2\2\63\u00e6\3\2\2\2\65\u00ef\3\2\2\2\67")
        buf.write("\u00f4\3\2\2\29\u00f8\3\2\2\2;\u00fe\3\2\2\2=\u0101\3")
        buf.write("\2\2\2?\u0108\3\2\2\2A\u010c\3\2\2\2C\u0111\3\2\2\2E\u0114")
        buf.write("\3\2\2\2G\u011a\3\2\2\2I\u011f\3\2\2\2K\u0125\3\2\2\2")
        buf.write("M\u012c\3\2\2\2O\u012e\3\2\2\2Q\u0130\3\2\2\2S\u0132\3")
        buf.write("\2\2\2U\u0134\3\2\2\2W\u0136\3\2\2\2Y\u0138\3\2\2\2[\u013a")
        buf.write("\3\2\2\2]\u013c\3\2\2\2_\u0143\3\2\2\2a\u0145\3\2\2\2")
        buf.write("c\u014e\3\2\2\2eg\t\2\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2")
        buf.write("\2hi\3\2\2\2ij\3\2\2\2jk\b\2\2\2k\4\3\2\2\2lm\7\61\2\2")
        buf.write("mn\7,\2\2nr\3\2\2\2oq\13\2\2\2po\3\2\2\2qt\3\2\2\2rs\3")
        buf.write("\2\2\2rp\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7,\2\2vw\7\61\2")
        buf.write("\2wx\3\2\2\2xy\b\3\2\2y\6\3\2\2\2z{\7\61\2\2{|\7\61\2")
        buf.write("\2|\u0080\3\2\2\2}\177\n\3\2\2~}\3\2\2\2\177\u0082\3\2")
        buf.write("\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3")
        buf.write("\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084\b\4\2\2\u0084\b")
        buf.write("\3\2\2\2\u0085\u0087\t\4\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\n\3\2\2\2\u008a\u008c\t\5\2\2\u008b\u008d\5\23")
        buf.write("\n\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f")
        buf.write("\3\2\2\2\u008e\u0090\t\4\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\f\3\2\2\2\u0093\u0095\5\t\5\2\u0094\u0096\7\60")
        buf.write("\2\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0098\5\13\6\2\u0098\u00a7\3\2\2\2\u0099")
        buf.write("\u009b\5\t\5\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u009d\7\60\2\2\u009d\u009f")
        buf.write("\5\t\5\2\u009e\u00a0\5\13\6\2\u009f\u009e\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a7\3\2\2\2\u00a1\u00a2\5\t\5\2")
        buf.write("\u00a2\u00a4\7\60\2\2\u00a3\u00a5\5\13\6\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6")
        buf.write("\u0093\3\2\2\2\u00a6\u009a\3\2\2\2\u00a6\u00a1\3\2\2\2")
        buf.write("\u00a7\16\3\2\2\2\u00a8\u00ae\7$\2\2\u00a9\u00aa\7^\2")
        buf.write("\2\u00aa\u00ad\t\6\2\2\u00ab\u00ad\n\7\2\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7$\2\2\u00b2\u00b3\b")
        buf.write("\b\3\2\u00b3\20\3\2\2\2\u00b4\u00b5\7-\2\2\u00b5\22\3")
        buf.write("\2\2\2\u00b6\u00b7\7/\2\2\u00b7\24\3\2\2\2\u00b8\u00b9")
        buf.write("\7,\2\2\u00b9\26\3\2\2\2\u00ba\u00bb\7#\2\2\u00bb\30\3")
        buf.write("\2\2\2\u00bc\u00bd\7~\2\2\u00bd\u00be\7~\2\2\u00be\32")
        buf.write("\3\2\2\2\u00bf\u00c0\7#\2\2\u00c0\u00c1\7?\2\2\u00c1\34")
        buf.write("\3\2\2\2\u00c2\u00c3\7>\2\2\u00c3\36\3\2\2\2\u00c4\u00c5")
        buf.write("\7>\2\2\u00c5\u00c6\7?\2\2\u00c6 \3\2\2\2\u00c7\u00c8")
        buf.write("\7?\2\2\u00c8\"\3\2\2\2\u00c9\u00ca\7\61\2\2\u00ca$\3")
        buf.write("\2\2\2\u00cb\u00cc\7\'\2\2\u00cc&\3\2\2\2\u00cd\u00ce")
        buf.write("\7(\2\2\u00ce\u00cf\7(\2\2\u00cf(\3\2\2\2\u00d0\u00d1")
        buf.write("\7?\2\2\u00d1\u00d2\7?\2\2\u00d2*\3\2\2\2\u00d3\u00d4")
        buf.write("\7@\2\2\u00d4,\3\2\2\2\u00d5\u00d6\7@\2\2\u00d6\u00d7")
        buf.write("\7?\2\2\u00d7.\3\2\2\2\u00d8\u00d9\7d\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7p\2\2\u00df\60")
        buf.write("\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7m\2\2\u00e5\62")
        buf.write("\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee\64")
        buf.write("\3\2\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7g\2\2\u00f3\66\3\2\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7t\2\2\u00f78\3")
        buf.write("\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7v\2\2\u00fd:\3")
        buf.write("\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7h\2\2\u0100<\3")
        buf.write("\2\2\2\u0101\u0102\7t\2\2\u0102\u0103\7g\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7w\2\2\u0105\u0106\7t\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107>\3\2\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7v\2\2\u010b@\3\2\2\2\u010c\u010d")
        buf.write("\7x\2\2\u010d\u010e\7q\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110B\3\2\2\2\u0111\u0112\7f\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113D\3\2\2\2\u0114\u0115\7y\2\2\u0115\u0116")
        buf.write("\7j\2\2\u0116\u0117\7k\2\2\u0117\u0118\7n\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119F\3\2\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7t\2\2\u011c\u011d\7w\2\2\u011d\u011e\7g\2\2\u011eH\3")
        buf.write("\2\2\2\u011f\u0120\7h\2\2\u0120\u0121\7c\2\2\u0121\u0122")
        buf.write("\7n\2\2\u0122\u0123\7u\2\2\u0123\u0124\7g\2\2\u0124J\3")
        buf.write("\2\2\2\u0125\u0126\7u\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7t\2\2\u0128\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7i\2\2\u012bL\3\2\2\2\u012c\u012d\7]\2\2\u012dN\3\2\2")
        buf.write("\2\u012e\u012f\7_\2\2\u012fP\3\2\2\2\u0130\u0131\7*\2")
        buf.write("\2\u0131R\3\2\2\2\u0132\u0133\7+\2\2\u0133T\3\2\2\2\u0134")
        buf.write("\u0135\7}\2\2\u0135V\3\2\2\2\u0136\u0137\7\177\2\2\u0137")
        buf.write("X\3\2\2\2\u0138\u0139\7=\2\2\u0139Z\3\2\2\2\u013a\u013b")
        buf.write("\7.\2\2\u013b\\\3\2\2\2\u013c\u0140\t\b\2\2\u013d\u013f")
        buf.write("\t\t\2\2\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141^\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0143\u0144\13\2\2\2\u0144`\3\2\2\2\u0145")
        buf.write("\u014b\7$\2\2\u0146\u0147\7^\2\2\u0147\u014a\t\6\2\2\u0148")
        buf.write("\u014a\n\7\2\2\u0149\u0146\3\2\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014cb\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0154")
        buf.write("\7$\2\2\u014f\u0150\7^\2\2\u0150\u0153\t\n\2\2\u0151\u0153")
        buf.write("\n\13\2\2\u0152\u014f\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\7")
        buf.write("^\2\2\u0158\u0159\n\6\2\2\u0159d\3\2\2\2\25\2hr\u0080")
        buf.write("\u0088\u008c\u0091\u0095\u009a\u009f\u00a4\u00a6\u00ac")
        buf.write("\u00ae\u0140\u0149\u014b\u0152\u0154\4\b\2\2\3\b\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    LINE_COMMENT = 3
    INTLIT = 4
    Exponent = 5
    FLOATLIT = 6
    STRINGLIT = 7
    PLUS = 8
    SUB = 9
    MUL = 10
    NOT = 11
    OR = 12
    DIF = 13
    LESS = 14
    LESS_EQUAL = 15
    ASSIGN = 16
    DIV = 17
    MOD = 18
    AND = 19
    EQUAL = 20
    GREATER = 21
    GREATER_EQUAL = 22
    BOOLEAN = 23
    BREAK = 24
    CONTINUE = 25
    ELSE = 26
    FOR = 27
    FLOAT = 28
    IF = 29
    RETURN = 30
    INTTYPE = 31
    VOID = 32
    DO = 33
    WHILE = 34
    TRUE = 35
    FALSE = 36
    STRING = 37
    LS = 38
    RS = 39
    LB = 40
    RB = 41
    LP = 42
    RP = 43
    SEMI = 44
    CM = 45
    ID = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", 
            "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'boolean'", "'break'", 
            "'continue'", "'else'", "'for'", "'float'", "'if'", "'return'", 
            "'int'", "'void'", "'do'", "'while'", "'true'", "'false'", "'string'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "LINE_COMMENT", "INTLIT", "Exponent", "FLOATLIT", 
            "STRINGLIT", "PLUS", "SUB", "MUL", "NOT", "OR", "DIF", "LESS", 
            "LESS_EQUAL", "ASSIGN", "DIV", "MOD", "AND", "EQUAL", "GREATER", 
            "GREATER_EQUAL", "BOOLEAN", "BREAK", "CONTINUE", "ELSE", "FOR", 
            "FLOAT", "IF", "RETURN", "INTTYPE", "VOID", "DO", "WHILE", "TRUE", 
            "FALSE", "STRING", "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", 
            "CM", "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "COMMENT", "LINE_COMMENT", "INTLIT", "Exponent", 
                  "FLOATLIT", "STRINGLIT", "PLUS", "SUB", "MUL", "NOT", 
                  "OR", "DIF", "LESS", "LESS_EQUAL", "ASSIGN", "DIV", "MOD", 
                  "AND", "EQUAL", "GREATER", "GREATER_EQUAL", "BOOLEAN", 
                  "BREAK", "CONTINUE", "ELSE", "FOR", "FLOAT", "IF", "RETURN", 
                  "INTTYPE", "VOID", "DO", "WHILE", "TRUE", "FALSE", "STRING", 
                  "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", "CM", "ID", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


