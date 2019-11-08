#ifndef FLOM_RADIO_ENDPOINT_H_
#define FLOM_RADIO_ENDPOINT_H_

#include <RF24.h>
#include <hive_map.hpp>

class RadioEndPoint: public hmap::network::non_blocking::EndPoint {
public:
    RadioEndPoint():
            m_radio(7, 8){ }
    void setup(const byte address[6]) {
        m_radio.begin();
        m_radio.openReadingPipe(0,address);
        m_radio.openWritingPipe(address);
        m_radio.startListening();
        m_radio.setPALevel(RF24_PA_MIN);
    }
    void broadcast(char* data, size_t len) override {
        m_radio.stopListening();
        m_radio.write(data, len);
        m_radio.startListening();
    }
    size_t deliver(char* data, size_t len) override{
        if(m_radio.available()){
            m_radio.read(data, len);
            return len;
        }
        return 0;
    }
private:
    RF24 m_radio; 
};

#endif