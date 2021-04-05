class DevicesController < ApplicationController

  def set_static
    load_device
    @device.set_static(params[:animation])
  end

  private

  def load_device
    @device = Device.find(params[:id])
  end

end