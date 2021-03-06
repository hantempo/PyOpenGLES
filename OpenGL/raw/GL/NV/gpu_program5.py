'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_gpu_program5'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_gpu_program5',False)
_p.unpack_constants( """GL_MAX_GEOMETRY_PROGRAM_INVOCATIONS_NV 0x8E5A
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_NV 0x8E5B
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_NV 0x8E5C
GL_FRAGMENT_PROGRAM_INTERPOLATION_OFFSET_BITS_NV 0x8E5D
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_NV 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_NV 0x8E5F
GL_MAX_PROGRAM_SUBROUTINE_PARAMETERS_NV 0x8F44
GL_MAX_PROGRAM_SUBROUTINE_NUM_NV 0x8F45""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glProgramSubroutineParametersuivNV( target,count,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLuintArray)
def glGetProgramSubroutineParameteruivNV( target,index,param ):pass


def glInitGpuProgram5NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
