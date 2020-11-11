# Todor's Notes on Automated CogAlg code analysis and generation
# 20-4-2019
#The * Map section below includes general incremental processing primitives

* Find entry point, function calls within available from the CogAlg code
* CogAlg code in local files, in imported files from the library of local files (not Python, Numpy etc.)

*Recognize functions and their headers:

def image_to_blobs(image):  # root function, postfix '_' denotes array vs element, prefix '_' denotes higher- vs lower- line variable

def comp_pixel(p__):  # bilateral comparison between vertically and horizontally consecutive pixels within image

def form_P_(dert_):  # horizontally cluster and sum consecutive pixels and their derivatives into Ps

def scan_P_(P_, seg_, frame):  # integrate x overlaps (forks) between same-sign Ps and _Ps into blob segments

def form_seg_(y, P_, frame):  # convert or merge every P into segment, merge blobs

def form_blob(term_seg, frame):  # terminated segment is merged into continued or initialized blob (all connected segments)

* Take into account comments and keywords ... bilateral, horizontally, overlaps, convert ... terminate ... segment ... merged ...

* Entry point segment:

frame_of_blobs = image_to_blobs(image)

* Take into account prefix, suffix, ... as types (but check code as well)...

* Basic types: scalar (known type), tuple (length, types, content - assigned idents, ...), list (length, content ... as types) - draw trees, graphs ...

* Import files: from intra_comp import intra_comp, hypot_g

* Import files: from comp_range import comp_range

* Simulate iterations, understand enumerate, zip, ...
# for i, blob in enumerate(frame_of_blobs[1]):
#    intra_comp(blob, hypot_g, rdn=0)

* Implant some used functions, like image.shape ...
# frame = [[0, 0, 0, 0], [], image.shape]  # params, blob_, shape

* SCOPES: global, local, ... Watch where vars are defined ... 

* frame = LIST(3).LIST(4).List(0),image.shape ...

* def comp_pixel(p__): ... list of list (_ _)

* dert__...[0] = p__ //pixels

[1] = dy__ #y__
[2] = dx__ #x__
[3] = g  #g__

*  i, dy, dx, g = dert_[1]  # first dert
   x0, L, I, Dy, Dx, G = 1, 1, i, dy, dx, g  # P params
   P_dert_ = [(i, dy, dx, g)]
   _s = g > 0  # sign # CONDITION... _s - previous, pre-underscore

* Cycles, Iterations: Init previous and current _var, var ...
# before main iterations (for, while, ...) 
#    _s = g > 0  # sign
#    for x, (i, dy, dx, g) in enumerate(dert_[2:-1], start=2):
#         s = g > 0

* Parse functions: arguments, local variables, order ... before-after
* counterparts: _s, s, _lx, lx, _x, x, _y, y ...
*  def form_P_(dert_): 
*    P_.append([_s, x0, L, I, Dy, Dx, G, P_dert_])  # last P in row
*    return P_

* Unfold cycles ... > ... + - ... rising, falling, ... sign
* P_ = scan_P_(P_, seg_, frame)
* if P_ and seg_:  # if both are not empty -- if possible to be empty
#     if P_ and seg_:  # if both are not empty
#        P = P_.popleft()  # input-line Ps
#        seg = seg_.popleft()  # higher-line segments,
#        _P = seg[2][-1]  # last element of each segment is higher-line P

* Find seg assignments with explicit variables

* blob = [s, [0] * (len(params) + 1), [], 1, [y, x0, xn]]  
# s, params,  seg_, open_segments, box
* new_seg = [y, [1] + params, [P], 0, fork_, blob]  
# y0, params, Py_, roots, fork_, blob

* Compute number of params in a list: [1] = list, len = 1 (len) + len(params) ...  

# form_seg_(y, P_, frame):  # convert or merge every P into segment, merge blobs

* for seg in seg_:
    if not seg is fork:
    seg[5] = blob  # blobs in other forks are references to blob in the first fork
    blob[2].append(seg)  # buffer of merged root segments
# How to generate it?
# Generate from the container (seg_)
# Naming from the container (remove suffix)
# ...  blob = fork_[0][5]
#           ...
   for fork in fork_[1:len(fork_)]:  # merge blobs of other forks into blob of 1st fork
        if fork[3] == 1:
                        form_blob(fork, frame)

    # 1:len(fork_)  # range ... 0 is loaded already fork_[0] ... 
#
# blob[3] += open_segs ... # List + = append to list, length >
    blob[4][0] = min(blob[4][0], box[0])  # extend box y0
    blob[4][1] = min(blob[4][1], box[1])  # extend box x0
    blob[4][2] = max(blob[4][2], box[2])  # extend box xn
    
# min == "left",  max == "right

 def form_blob(term_seg, frame):  # terminated segment is merged into continued or initialized blob (all connected segments)
#    s, [Ly, L, I, Dy, Dx, G], seg_, open_segs, (y0, x0, xn) = blob|

# ... yn = y0s + params[0]  # yn = y0 + Ly
# yn > y0 (Ly > 0), right
                                    
# ?WCBD? ?WW (What is wanted + WCBD)

* Container: ITERATE

   if not blob[3]:  # if open_segments == 0: blob is terminated and packed in frame
        s, [Ly, L, I, Dy, Dx, G], seg_, open_segs, (y0, x0, xn) = blob
        yn = y0s + params[0]  # yn = y0 + Ly
        map = np.zeros((yn - y0, xn - x0), dtype=bool)  # local map of blob
        for seg in seg_:
          ...
          
* Map

# WHAT is?
@ WHY?

-- coordinates, selection

* PRINCIPLES
 -- SELECTION
  -- HOW? -- CONDITIONS: ...
                 --- IF ... different values ...
                 
 -- INCREMENTAL
  -- WHAT?
   -- PRIMARY: COORDINATES, INPUT
   
 -- DIMENSIONS (Knowledge how to represent them)
  0D: Variable  #scalar
  1D: List      #vector
  1D: Tuple
  1D+Idents: Namedtuple #connected to idents
  2D: Numpy array : shape, ... -> mapping to 1D, to 0D ... coordinates
      Initializations, types, ... .zeros, .ones, ... .shape ... dtype=int, dtype=bool
        --- bool is primary selection=differentiation type, IF

  -- ADDRESSING
    -- Ident (Scope)
      List of lists
      NP arrays      
      Indexing: Numpy array ~ Multi-dimensional lists
      
  -- ITERATIONS
    -- Generalized definitions of the traversal
       Traverse(source=dert__, start_index= , set = ...from=) 
       #?will it be shorter than the full code?
       
    -- Unfold/Have templates for one by one setting
    -- Then compress (if possible) - can be manual
    
       Summation:  [Target summation addresses frame[0] ...  ]
         frame[0][0] += I
         frame[0][1] += Dy
         frame[0][2] += Dx
         frame[0][3] += G
         
    -- COUNTING
         -- During iterations, scanning
            +1 ...
            
    -- RANGES
        -- start, end
        -- minimum, maximum
        -- left, right  x0, xn; y0, yn
        
    -- GROUP by Identifiers
       x: x, x0, _x, _x0, xn, _xn
       y: y, y0, _y, _y0, yn, _yn
       
        
         
# 21-4-2019
@ScanTo(_dert, _li, _lx)
@InsideIs(_dert_, _li, _lx, incl)


    
 
      
         
  
  
  
   
                 
 
# 
          

