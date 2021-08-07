class DevicesController < ApplicationController

  def set_static
    load_device
    @device.set_static(params[:animation])
  end

  def set_random
    load_device
    @device.set_random
  end


  private

  def load_device
    @device = Device.find(params[:id])
  end

end