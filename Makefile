# compile options
FC = gfortran
FCFLAGS = -O3
FLIBS = 
IPATH = 
OBJS = stats.o
MAIN = test_stats.f90

# main program compilation
test_stats : $(MAIN) $(OBJS)
	$(FC) $(FCFLAGS) -o $@ $^ $(IPATH) $(FLIBS)

# object files
%.o : %.f90
	$(FC) $(FCFLAGS) -c $< $(IPATH) $(FLIBS)

# clean
clean :
	rm *.o *.mod
