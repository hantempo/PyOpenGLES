'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_pixel_data_range'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_pixel_data_range',False)
_p.unpack_constants( """GL_WRITE_PIXEL_DATA_RANGE_NV 0x8878
GL_READ_PIXEL_DATA_RANGE_NV 0x8879
GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV 0x887A
GL_READ_PIXEL_DATA_RANGE_LENGTH_NV 0x887B
GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV 0x887C
GL_READ_PIXEL_DATA_RANGE_POINTER_NV 0x887D""", globals())
glget.addGLGetConstant( GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV, (1,) )
glget.addGLGetConstant( GL_READ_PIXEL_DATA_RANGE_LENGTH_NV, (1,) )
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glPixelDataRangeNV( target,length,pointer ):pass
@_f
@_p.types(None,_cs.GLenum)
def glFlushPixelDataRangeNV( target ):pass


def glInitPixelDataRangeNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
