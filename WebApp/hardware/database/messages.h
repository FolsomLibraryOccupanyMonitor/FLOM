#ifndef ROOMS_MESSAGES_H_
#define ROOMS_MESSAGES_H_
//Basic car structure
//Needs to include Gerg's header from Hive Map
//Contains: ID, Color, Heading, GasLevel, speed

#include <hive_map.hpp>
#include <message.h>
#include "locations.h"

// message constants
#define OCCUPANCY_MSG 12 //10 or higher

namespace occupancy {

struct Body {
  bool occupied = false;
  unsigned char roomID = 0;
};

struct Msg{
  hmap::msg::Header header {
      .type = OCCUPANCY_MSG,
      .bcast_radius = 1,
      .destination = hmap::loc::ANY,
      .size = sizeof(Msg)
  };
  Body body;
  unsigned char type = OCCUPANCY_MSG;
};

}
#endif //COUNTRY_ROADS_HARDWARE_MESSAGES_H_
