
/* analysis on neighbours
 such as number of neighbours */

//////////////////////////////////////////////////////////////////////////////////////////////////////////

#pragma once

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <tuple>

#include "data_structures.hpp"
#include "basic.hpp"
#include "read_write.hpp"

//////////////////////////////////////////////////////////////////////////////////////////////////////////

template<class T>
class AnalyseNeighbours : public Analyser {
public:
  
  T sim;
  Beads *beads;
  
  AnalyseNeighbours(T sim_, Beads *beads_);
  ~AnalyseNeighbours();
  tuple<double, double> AnalyseNeighbours::perform_analysis ();
  void write_analysis_results(double data, string outfilepath);

  void AnalyseNeighbours::build_linked_cell_list(const double * const *x,
                                                 const double * const *y,
                                                 vector<int> & heads,
                                                 vector<int> & llist,
                                                 const double wbin, const int nboxes,
                                                 const int nsize, const int step,
                                                 const int natoms, const double l);
  set<int> AnalyseNeighbours::get_neighs_of_a_cell (const int start, const int end,
                                                    const double * const *x,
                                                    const double * const *y,
                                                    const int step, const double rcut,
                                                    const int nboxes,
                                                    const double lx, const double ly,
                                                    const vector<int> & cid,
                                                    const vector<int> & heads,
                                                    const vector<int> & llist);
  map<int, set<int> > AnalyseNeighbours::build_neigh_list (const double * const *x,
                                                           const double * const *y,
                                                           const vector<int> & cid,
                                                           const vector<int> & nbpp,
                                                           const vector<int> & heads,
                                                           const vector<int> & llist,
                                                           const int npols,
                                                           const double rcut,
                                                           const int nsteps,
                                                           const int step,
                                                           const int nboxes,
                                                           const double lx,
                                                           const double ly);
  tuple<double, double> AnalyseNeighbours::calc_num_neighbours (const double * const *x,
                                                                const double * const *y);
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////